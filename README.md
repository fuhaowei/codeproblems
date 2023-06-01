# codeproblems

Here a sample repository of the leetcode problems I have tackled, and my basic strategies towards being able to identify and categorise solutions into solving then.


## general python pointers:

To use, we assume that the file "file.in" contains two integers separated by whitespace.

```
import sys

sys.stdin = open("file.in", 'r')
sys.stdout = open("file.out", 'w')

# Define the input and intput functions
input = lambda: sys.stdin.readline().strip()
intput = lambda: map(int, input().split())

# Read two integers from input and compute their sum
a, b = intput()
sum = a + b

# Write the sum to output
print(sum) 

```

More examples on how to use

```
if __name__  == "__main__":

    #reads string from input function, assings to s
    s = input()

    # This line uses the intput function to read a single integer value from input.
    
    # The trailing comma after N is used to unpack the single element from the iterable returned by intput and assign it directly to the variable N.

    N, = intput()

    #this line uses the intput function to read three integer values from input, which are then unpacked and assigned to the variables x, y, and z respectively.
    x, y, z = intput()

    #Here, the intput function is used to read multiple integer values from input, and the resulting iterable is converted into a list using the [*iterable] syntax. The list is assigned to the variable A.
    A = [ *intput() ]

    # generating a 2d array
    B = [ [*intput()] for _ in range(N)]

```