# Python class and Objects 
class Dog:
    attr1 = "Mammal"
    attr2 = "Dog"
    
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
        
Roger = Dog()

print(Roger.attr1)
Roger.fun()
