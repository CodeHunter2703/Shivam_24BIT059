s="anagram"
t="magranap"
ls=list(s)
lt=list(t)
def duplicater(ls,lt,f=""):
    for i in ls:
        for j in lt:
            if i == j:
                f=f+j
                print(f)
                lt.remove(j)
                break
            else:
                f=f+j
    
    return f
def Cheker(s,f):
    if s==f:
        print ("thet given strings are anagram")
    else:
        print("?")

f=duplicater(ls,lt)
Cheker (s,f)
            
