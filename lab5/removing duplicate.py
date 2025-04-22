# Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list
from random import random, randint
def duplicate(lst1):
    set1=set(lst1)
    l=list(set1)
    return set1
lst=[randint(0,30) for i in range(51) ]
print(f"the parent list is {lst}")
print(f"the removing of duplicate then \n {duplicate(lst)}")
