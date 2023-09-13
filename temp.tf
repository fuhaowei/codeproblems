###########################################################################
# Template for Task 3 AWS AutoScaling Test                                #
# Do not edit the first section                                           #
# Only edit the second section to configure appropriate scaling policies  #
###########################################################################

############################
# FIRST SECTION BEGINS     #
# DO NOT EDIT THIS SECTION #
############################
locals {
  common_tags = {
    Project = "vm-scaling"
  }
  asg_tags = {
    key                 = "Project"
    value               = "vm-scaling"
    propagate_at_launch = true
  }
}

provider "aws" {
  region = "us-east-1"
}


resource "aws_security_group" "lg" {
  # HTTP access from anywhere
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.common_tags
}

resource "aws_security_group" "elb_asg" {
  # HTTP access from anywhere
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.common_tags
}

######################
# FIRST SECTION ENDS #
######################

############################
# SECOND SECTION BEGINS    #
# PLEASE EDIT THIS SECTION #
############################

# Step 1:
# TODO: Add missing values below
# ================================
resource "aws_launch_template" "lt" {
  name          = "ws_lt"
  image_id      = "ami-09400c18bd0c0f94f"
  instance_type = "m5.large"

  monitoring {
    enabled = true
  }

  vpc_security_group_ids = [aws_security_group.elb_asg.id]

  tag_specifications {
    resource_type = "instance"
    tags = {
      Project = "vm-scaling"
    }
  }
}

data "aws_vpc" "default" {
  default = true
}


// -> add default VPC_id here (aws default vpc resource)
resource "aws_subnet" "my_subnet" {
  vpc_id                  =  data.aws_vpc.default.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "my-subnet"
    Project = "vm-scaling"
  }
}


# Create an auto scaling group with appropriate parameters
# TODO: fill the missing values per the placeholders
resource "aws_autoscaling_group" "asg" {
  availability_zones        = ["us-east-1a"]
  max_size                  = 3
  min_size                  = 1
  desired_capacity          = 2
  default_cooldown          = 60
  health_check_grace_period = 30
  health_check_type         = "EC2"
  launch_template {
    id = aws_launch_template.lt.id
  }
  target_group_arns = [aws_lb_target_group.tf-tg.arn]
  tag {
    key                 = local.asg_tags.key
    value               = local.asg_tags.value
    propagate_at_launch = local.asg_tags.propagate_at_launch
  }
}

# TODO: Create a Load Generator AWS instance with proper tags

resource "aws_instance" "load_generator" {
  ami           = "ami-0d196471a996e58d6"
  instance_type = "m5.large"

  vpc_security_group_ids = [aws_security_group.lg.id]

  key_name = "cloudclasskeypair"

  subnet_id = "subnet-07c631d7d419d312d"

  tags = local.common_tags
}


# Step 2:
# TODO: Create an Application Load Balancer with appropriate listeners and target groups
# The lb_listener documentation demonstrates how to connect these resources
# Create and attach your subnet to the Application Load Balancer 
#
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_listener
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_target_group

resource "aws_lb" "tf-lb" {
  name               = "tf-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.elb_asg.id]
  subnets            = ["subnet-07c631d7d419d312d", "subnet-0f9ca819eeff99c74"]

  enable_deletion_protection = false

  tags = local.common_tags
}

#create target group
resource "aws_lb_target_group" "tf-tg" {
  name     = "tf-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = "vpc-0d7aa5f9d053dbee9"

  health_check {
    enabled           = true
    interval          = 30
    path              = "/"
    timeout           = 5
    healthy_threshold = 3
  }
}

#create listener
resource "aws_lb_listener" "tf-listener" {
  load_balancer_arn = aws_lb.tf-lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_lb_target_group.tf-tg.arn
    type             = "forward"
  }
}


# Step 3:
# TODO: Create 2 policies: 1 for scaling out and another for scaling in
# Link it to the autoscaling group you created above
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/autoscaling_policy

 resource "aws_autoscaling_policy" "scale_in_policy" {
    name = "scale_in_policy"
    scaling_adjustment = -1
    adjustment_type = "ChangeInCapacity"
    cooldown = 20
    autoscaling_group_name = aws_autoscaling_group.asg.name
 }

resource "aws_autoscaling_policy" "scale_out_policy" {
  name                   = "scale_out_policy"
  scaling_adjustment     = 1
  adjustment_type        = "ChangeInCapacity"
  cooldown               = 20
  autoscaling_group_name = aws_autoscaling_group.asg.name
}


# Step 4:
# TODO: Create 2 cloudwatch alarms: 1 for scaling out and another for scaling in
# Link it to the autoscaling group you created above
# Don't forget to trigger the appropriate policy you created above when alarm is raised
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_metric_alarm


resource "aws_cloudwatch_metric_alarm" "scale_out_alarm" {
  alarm_name          = "scale_out_alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "RequestCount"
  namespace           = "AWS/ApplicationELB"
  period              = "60"
  statistic           = "Maximum"
  threshold           = "0.6"
  alarm_description   = "This metric triggers scale out policy"
  alarm_actions       = [aws_autoscaling_policy.scale_out_policy.arn]
  dimensions = {
    AutoScalingGroupName = aws_autoscaling_group.asg.name
  }
}

resource "aws_cloudwatch_metric_alarm" "scale_in_alarm" {
  alarm_name          = "scale-in-alarm"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "300"
  statistic           = "Average"
  threshold           = "20"
  alarm_actions       = [aws_autoscaling_policy.scale_in_policy.arn]
  dimensions = {
    AutoScalingGroupName = aws_autoscaling_group.asg.name
  }
}



######################################
# SECOND SECTION ENDS                #
# MAKE SURE YOU COMPLETE ALL 4 STEPS #
######################################
