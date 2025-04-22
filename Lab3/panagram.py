def ispanagram(str):
    l=[]
    for i in str:
        if i not in l:
            l.append(i)
    print(l)
    print(len(l))
    idx=0
    while idx<len(l):
        if l[idx] in str:
            removed=l.pop(idx)
            print(removed)
        else:
            idx+=1
    print(l)
    if len(l)==27:
        return  True
    else :
        return False
if ispanagram("qwtyuiopzxcvbnm"):
    print("the string is a panagram")
else:
    print("not psnsgram")
