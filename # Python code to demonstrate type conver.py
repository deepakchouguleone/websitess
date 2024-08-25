# Python code to demonstrate type conversion using dict, complex, str

a = 1 
b = 2

# Initialize tuple 
tup = (('a', 1), ('f', 2), ('g', 3))

# Printing integer converting to complex number 
c = complex(1,2)
print("After converting integer to complex number:",end="")
print(c)

# Print Integer Converting to String 
c = str(a)
print("After converting integer to string:",end="")
print(c)

# Print tuple converting to dictionary
d = dict(tup)
print("After converting tuple to dictionary:",end="")
print(d)
