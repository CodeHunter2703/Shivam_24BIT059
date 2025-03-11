def intersector(lst1,lst2):
    # lst1.extend(lst2)
    # lst1=list(set(lst1))
    idx=0
    while idx< len(lst2):
        if lst2[idx] in lst1:
            idx+=1
        else:
            lst2.pop(idx)


    return lst2
l=intersector(lst1=[1,2,3,4,4,5,6,6,6,456,7,34,56,67,6,543,76,5432,6432],lst2=[432,543,432,2,1,3,4,5,7,6,34,2])
print(l)