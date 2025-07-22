class square:

    def __init__(self,side):
 
        
    def area(self):
        print("my area is = " , self.side**2 )

class circle:
    def __init__(self,radius):#
        self.radius = radius

    def area(self):
        print("my area is =",3.14*self.radius*self.radius)


obsquare = square(5)
obcircle = circle(5) 


for result in (obsquare,obcircle):
    result.area()