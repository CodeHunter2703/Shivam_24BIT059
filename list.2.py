import random
def searcher(check,l):
    final_list=[]
    for idx,i in enumerate(l):
        if i == check:
            final_list+=[idx]
    return final_list




lst=[random.randint(0,100) for i in range(21) ]
print(lst)
n= int(input("Enter the number you want to get position of those occurences"))
print(f"the occurences are {searcher(n,lst)}")