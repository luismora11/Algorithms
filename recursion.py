#This is an example of a recursive algorithm

def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n <= 1:
        return 1
    else:
        return n * get_recursive_factorial(n-1)




def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

print(get_recursive_factorial(6))
print(get_iterative_factorial(6))



#Example number 2

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    
    return get_fib(position - 1) + get_fib(position - 2)

    
    
    
    
    return -1



