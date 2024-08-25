# Write a function to add two numbers and return a value
def add(a, b):
    return a + b


# Write a function which asks users to provide a number to find factorial 
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))