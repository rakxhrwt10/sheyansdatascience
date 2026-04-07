class Students:
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks 
    
    def __str__(self):
        return f"{self.name} is your name and your marks are {self.marks}"

obj = Students("Akarsh",95)

print(obj)

class Shopping:
    def __init__(self,items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

obj = Shopping(['apple',"milk","bread"])
obj2  = Shopping(["apple","banana"])

print(len(obj2))

class Numbers:
    def __init__(self,number):
         self.number = number 
        
    def __add__(self,custom):
        return self.number + custom.number


obj1 = Numbers(12)
obj2 = Numbers(34)

print(obj1 + obj2)