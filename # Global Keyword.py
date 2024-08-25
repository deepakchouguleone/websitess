# Global Keyword 
def f():
    global s 
    s += "Me inside the function"
    print(s)
    
# Global scope 
s = "I love coding in Python"
print(s)
f()