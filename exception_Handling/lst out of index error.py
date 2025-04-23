l=[1,2,3,4,5,6,7,8]
try:
    for i in range(0,len(l)):
        print(f"pair is {(l[i],l[i+1])}")
except:
    print("Out of index error")
smallest="catholic"
for i in range(len(smallest)):
    for j in range(len(smallest)):
        if j+i==len(smallest)+1 and i>0 :
            break
        print(smallest[j:j+i])
