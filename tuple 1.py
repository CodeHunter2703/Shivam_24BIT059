lst=[("bro","brooo","brother","bhaijan"),"sister","behen","didi","aunty","aurat",('man','boy')]
boy=0
girl=0
for i in lst:
    if isinstance(i,tuple)==True:
        l=len(i)
        boy+=l
    else:
        girl+=1
print (f" the numbers of girls {girl} and the number of boys {boy}")