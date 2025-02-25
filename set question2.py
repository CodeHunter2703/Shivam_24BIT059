# create a set of 10 random digits containing from 15 to 45
import random
count=0
set1=[]
set1=set(set1)
while len(set1)<10:
    set1.add(random.randint(15,45))
print(set1)
set1=list(set1)
set2=set1.copy()
for i in set2[:]:
    if i >35:
        count+=1
        set2.remove(i)
print(f"for the number greater then 35 in set {set1} are {count} \n after removing {set2}")