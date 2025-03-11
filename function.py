def create_array(x,y,z,n):
    result_array=[]
    for i in range(x):
        layer = []
        for j in range(y):
            row=[]
            for k in range(z):
                coloum = n
                row.append(coloum)
                layer.append((row))
                result_array.append(layer)


    return result_array
print(create_array(3,2,4,1))