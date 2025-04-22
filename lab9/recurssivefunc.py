def sanitize(l,idx=0):
    if idx==len(l):
        print(l)
        return l
    if l[idx] < 0:
        print(l[idx])
        l[idx]=0
        print(l[idx])
    return sanitize(l[:],idx+1)
s=input("enter the element  with " "")
s=s.split()
print(s)
lst=[int(i) for i in s]
print(lst)
result=sanitize(lst)
print(result)
    
