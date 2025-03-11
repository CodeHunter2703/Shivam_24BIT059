def create_array(end):
    l=[(i,i**2,i**3) for i in range(1,end+1)]
    return l
l=create_array(10)
print(l)