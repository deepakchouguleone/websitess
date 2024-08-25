# Using python Global and Local Variables 

a =1

# Uses Global because there is no local 'a'
def f():
    print("Inside f():", a)

# Variable 'a' is redefined as local
def g():
    a = 2
    print("Inside g():", a)
    
# Uses Global keyword to modify global 'a'
def h():
    global a 
    a = 3 
    print("Inside h():", a)

