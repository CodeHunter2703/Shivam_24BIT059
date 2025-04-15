l=["rat","cat","bat"]
s=l[0]
dcount={}
s.lower
for x in l:
    count={}
    for i in range(len(s)):
        for j in range(len(x)):
            check=x[j:j+i]
            
            print(check)
            if j+i== len(s):
                break