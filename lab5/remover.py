l=[1,2,3,4]
for i in l[:] :
    if i%2==0:
        l.remove(i)
    l.append(i)
    print(l)

print(l)
