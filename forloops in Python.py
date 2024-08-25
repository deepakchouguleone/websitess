# Python for loop
for i in range(10):
    print(i)
# Write a python function for finding prime numbers
def prime(n):
        if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
