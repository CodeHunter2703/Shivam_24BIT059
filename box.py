class box:

    def __init__(self,l=0,b=0):
        self.l,self.b=l,b
    def area(self):
        return self.l*self.b
    
class box1(box):
    area=0
    def __init__(self,h=0,a=0):
        self.a=a
        
        self.h=h
    
    def volume(self):
        return a *self.h
s=input("Enter the l b h with apaces btw")
s=s.split(" ")
s=[int(i) for i in s]
rec=box(s[0],s[1])
a=rec.area()
rec2=box1(s[-1],a)
v=rec2.volume()

print(a,v)

