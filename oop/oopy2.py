class fruits:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def intro(self):
        print("my favoratie fruit name is",self.name,"the color of fruit is",self.color)

banana = fruits('banana', 'yellow')

print(banana.name)
banana.intro()

    