# class complex_no:
#     a=[]
#     b=[]
    
#     def addn(self,other):
#         return str(self.a[0]+self.b[0]) +"+i" +"("+str(self.b[1]+self.a[1])+")"

# c1=input("Enter the 1 st complex no")
# c2=input("Enter the 2nd complex no:")
# c1=c1.split("+i" or "-i")
# c2=c2.split("+i" or "-i")
# print(c1,c2)
# obj1=complex_no()
# obj1.a=c1
# obj1.b=c2
# print(obj1.addn())
class ComplexNo:
    def __init__(self):
        self.a = []
        self.b = []
    
    def addn(self):
        
        real_sum = (self.a[0]) + (self.b[0])
        imag_sum = (self.a[1]) + int(self.b[1])
        return f"{real_sum}+i({imag_sum})"


c1 = input("Enter the 1st complex number: ")
c2 = input("Enter the 2nd complex number: ")

if "+i" in c1:
    c1 = c1.split("+i")
elif "-i" in c1:
    c1 = c1.split("-i")

if "+i" in c2:
    c2 = c2.split("+i") 
elif "-i" in c2:
    c2 = c2.split("-i")

obj1 = ComplexNo()
obj2 = ComplexNo()
print(c1,c2)
c1=[int(i) for i in c1]
c2=[int(i) for i in c2]
obj1.a=c1
obj1.b=c2
# Print the result of the addition
print(obj1.addn())
