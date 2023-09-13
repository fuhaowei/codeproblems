# first part:
# given a parsed mathematical equation with only ()+-*/, evaluate it
# There are parenthesis around every arithmetic op
# only exception checking is with division to make sure that you don't divide by 0, and we always want to result to be integer
# ie ((a+b)*c) get parsed to ['(', '(', a, '+', b, ')', '*', c, ')']


operands = ["+", "-", "*", "/"]


def get_expressions(inputs):
    """
    DO NOT COPY EXACTLY BECAUSE THIS IS WHAT I WROTE DURING THE PHONE SCREEN. I'M PRETTY SURE HE TOOK A COPY OF WHAT I WROTE BECAUSE HE HIGHLIGHTED EVERYTHING.
    """
    ans = []
    if len(inputs) == 1:
        return inputs[0]

    for split_idx in range(1, len(inputs)):
        inputs_lhs = inputs[:split_idx]
        inputs_rhs = inputs[split_idx:]

        exprs_lhs = get_expressions(inputs_lhs)
        exprs_rhs = get_expressions(inputs_rhs)

        for expr_lhs in exprs_lhs:
            for expr_rhs in exprs_rhs:
                for op in operands:
                    expr = "(" + expr_lhs + op + expr_rhs + ")"
                    ans.append(expr)

    return ans


def make_target(inputs, target):
    perms = itertools.permutations(inputs)
    for perm in perms:
        exprs = get_expressions(perm)
        for expr in exprs:  # TODO: catch exceptions to avoid short-circuiting
            if evaluate(expr) == target:
                return expr

    return None












# second part:
# given 4 numbers, can you put parenthesis, and +-*/ so that they make a given target value
# you can not reorder the numbers 









def evaluate(expr):
    def parse(expr):
        depth = 0
        for i,c in enumerate(expr):
            if c == '(':
                depth += 1
            if c == ')':
                depth -= 1
            if c in "+-*/" and depth == 1:
                return i, c
        return None

    def resolve(lhs, op, rhs):
        if op == '+': return lhs + rhs
        if op == '*': return lhs * rhs
        if op == '-': return lhs - rhs
        if op == '/':
            if rhs == 0:
                raise ZeroDivisionError("divide by 0")
            if lhs % rhs != 0:
                raise OSError("non-integer division")
            return lhs // rhs

    if expr.isnumeric():
        return int(expr) 
    
    op_idx, op = parse(expr)
    lhs = evaluate( expr[1:op_idx] )
    rhs = evaluate( expr[op_idx+1:-1] )
    return resolve(lhs, op, rhs)



# second part:
# given N numbers, can you put parenthesis, and +-*/ so that they make a given target value
# you can not reorder the numbers
def canMakeTarget(nums, target):
    operators = "+-*/"
    size = len(nums)
    num_ops = size - 1

    def gen_op_sets(i=0, ops=[0] * num_ops):
        if i == num_ops:
            yield ops
            return

        for op in operators:
            ops[i] = op
            for x in gen_op_sets(i + 1, ops):
                yield x

    def solve(ops):
        expr = nums + ops
        expr[::2] = nums
        expr[1::2] = ops

        def wrap(e):
            if len(e) == 1:  # e[0] is an int literal
                return e
            return ['('] + e + [')']

        def arrange(exprs):  # -> 'all possible parenthetical arrangements'
            if len(exprs) == 1:
                return [exprs]

            results = []
            for op_idx in range(1, len(exprs), 2):
                mid = exprs[op_idx]  # op
                lhs = exprs[:op_idx]
                rhs = exprs[op_idx + 1:]
                lhs_combos = arrange(lhs)
                rhs_combos = arrange(rhs)
                for l in lhs_combos:
                    for r in rhs_combos:
                        e = wrap(l) + [mid] + wrap(r)
                        results.append(e)
            return results

        for e in arrange(expr):
            e_str = ''.join(map(str,wrap(e)))
            try:
                x = evaluate(e_str)
                assert x == eval(e_str)
                if x == target:
                    return True
            except:
                pass

    return any( map( solve, gen_op_sets() ) )




# Arithmetic
# Part 1
# Given an expression consisting of numerical operands, operators, and **parentheses enclosing each operation**, compute the value.

# 1. The quotient of every division must be a positive integer.
# 2. The result of every subtraction must be a positive integer.

# Assume you're given an expression split(expr) that works like so:
# split("((4+3)*2)") -> ["(4+3), "*", "2"]
# split("4") -> None

# expr = "((14+3)*5)"
# nums = ["(", "(", 14, "+", 3, ")", "*", 5, ")"]

# a+b+c

# (a+(b+c))


def split(expr):
    depth = 0
    for i,c in enumerate(expr):
        if c == '(':
            depth += 1
        if c == ')':
            depth -= 1
        if c in "+-*/" and depth == 1:
            return expr[:i], c, expr[i+1:]
    return None

def evaluate(nums): 
    spl = split(nums)
    if spl == None:
        # nums is len 1 and it's a literal value
        return int(nums[0])

    lhs, op, rhs = split(nums)
    lhs = evaluate(lhs)
    rhs = evaluate(rhs)
    if op == "+":
        return lhs + rhs
    if op == "*":
        return lhs * rhs
    if op == "-":
        return lhs - rhs
    if op == "/":
        if lhs % rhs != 0:
            raise OSError() 
        if rhs == 0:
            raise ZeroDivisionError()
        return lhs // rhs
    
    




ß"""
Arithmetic
Part 1
Given an expression consisting of numerical operands, operators, and **parentheses enclosing each operation**, compute the value.

1. The quotient of every division must be a positive integer.
2. The result of every subtraction must be a positive integer.

Assume you're given an expression split(expr) that works like so:
split("((4+3)*2)") -> ["(4+3), "*", "2"]
split("4") -> None

expr = "((14+3)*5)"
nums = ["(", "(", 14, "+", 3, ")", "*", 5, ")"]

a+b+c

(a+(b+c))

"""

 def split(expr):
    depth = 0
    for i,c in enumerate(expr):
        if c == '(':
            depth += 1
        if c == ')':
            depth -= 1
        if c in "+-*/" and depth == 1:
            return expr[:i], c, expr[i+1:]
    return None

def evaluate(nums): 
    spl = split(nums)
    if spl == None:
        # nums is len 1 and it's a literal value
        return int(nums[0])

    lhs, op, rhs = split(nums)
    lhs = evaluate(lhs)
    rhs = evaluate(rhs)
    if op == "+":
        return lhs + rhs
    if op == "*":
        return lhs * rhs
    if op == "-":
        return lhs - rhs
    if op == "/":
        if lhs % rhs != 0:
            raise OSError() 
        if rhs == 0:
            raise ZeroDivisionError()
        return lhs // rhs

# given some numbers, can you put parenthesis, and +-*/ so that they make a given target value. may or may not be able to reorder the numbers, we dont know. you can not reorder the numbers 

def canMakeTarget(nums, target):
    operators = "+-*/"

    # return a list of strings that represent all the 
    # possible parenthetical groupings of the input 
    def groups(nums):
        if len(nums) == 1:
            return nums
        results = []
        for split in range(1, len(nums)):
            left  = groups( nums[:split] )
            right = groups( nums[split:] )
            for l in left:
                for r in right:
                    for op in operators:
                        res = "(" + l + op + r + ")" 
                        results.append(res)
        return results
            
    for expr in groups(nums):
        try:
            x = evaluate(expr)
            if x == target:
                return True
        except:
            pass
    return False
                
    




#can permutatet

def canMakeTarget(nums, target):
    operators = "+-*/"

    # return a list of strings that represent all the 
    # possible parenthetical groupings of the input 
    def groups(nums):
        if len(nums) == 1:
            return nums
        results = []
        for split in range(1, len(nums)):
            left  = groups( nums[:split] )
            right = groups( nums[split:] )
            for l in left:
                for r in right:
                    for op in operators:
                        res = "(" + l + op + r + ")" 
                        results.append(res)
        return results

    for p in itertools.permutations(nums):
        pnums = [*p]
        for expr in groups(pnums):
            try:
                x = evaluate(expr)
                if x == target:
                    return True
            except:
                pass
    return False