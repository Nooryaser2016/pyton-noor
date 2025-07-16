class parent:
    def __init__(self,eyes,smile):
        self.eyes = eyes
        self.smile = smile

    def display(self):
        print("the eyes color is",self.eyes)
        print("your smile is",self.smile)

class child(parent):
    def __init__(self, name, age, eyes, smile):
        self.name = name
        self.age = age
        
        super().__init__(eyes, smile)
a = child('hafedh',14,'blue','shiny')
a.display()

         