class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(self.name,"age is",self.age)


raja=student("raja",10)
max=student("max",13)
raja.intro()
max.intro()