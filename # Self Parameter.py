# Self Parameter
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        
        def show(self):
            print(self.name)
            print(self.company)

obj = GFG("John", "Geeksforgeeks")
obj.show()


