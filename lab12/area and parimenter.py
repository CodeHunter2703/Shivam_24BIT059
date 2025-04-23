class Box1:
    def __init__(self,length,width,height):
        self.length = length
        self.height = height
        self.width = width
    def area(self):
        return self.length * self.width
    def volume(self):
        return self.length * self.height * self.width
height = int(input("height"))
width = int(input("width"))
length = int(input("length"))
obj = Box1(length,width,height)
print("area",obj.area())
print("volume",obj.volume())
