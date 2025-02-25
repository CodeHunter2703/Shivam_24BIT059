set1=[]
set1=set(set1)
for i in range(5):
    ask=input(f"Enter the name {i+1} you want to add in the set")
    set1.add(ask)
mod=input("Enter the name you want to mod\n")
ex=input("instead of what name-->")
set1=list(set1)
for  idx,i in enumerate(set1):
    if i == ex:
        set1[idx]=mod
for i in range(2):
    destroy=input(f"Enter the name {i+1} you want to del")
    set1.remove(destroy)
set1=set(set1)
print(set1)