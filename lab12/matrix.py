class Matrix:
    m1=[]
    m2=[]
    print("summation")
    def addn(self):
        result=[]
        for i,j in zip(self.m1, self.m2):
            r=[]
            for x,y in zip(i,j):
                r+=[x+y]
            result+=[[r]]
        for i in result:
            print(str(i))
        return result
    print("Transpose")
    def trans(self):
        result=[]
        for j in range(3):
            r=[]
            for i in self.m1:
                r+=[i[j]]
            result+=[[r]]
        for i in result:
            print(str(i))
        return result

    def multiply(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                sum_product = 0
                for k in range(3):
                    sum_product += self.data[i][k] * other.data[k][j]
                row.append(sum_product)
            result.append(row)
        return Matrix(result)
        
m1=[]
m2=[]
print("for matrix 1")
for j in range(3):
    ask= input("Enter the 3 elements")
    lst=ask.split(" ")
    m1+=[[int(i) for i in lst]]
print(m1)
print("for matrix 2")
for j in range(3):
    ask= input("Enter the 3 elements")
    lst=ask.split(" ")
    m2+=[[int(i) for i in lst]]
#for displaying only
print("matrix one is ")
for i in m1:
    print(str(i))
print("matrix second is ")
for i in m2:
    print(str(i))

obj=Matrix()
obj.m1=m1
obj.m2=m2
obj.addn()
obj.trans()
