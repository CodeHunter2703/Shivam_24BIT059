
def removeDuplicates(n):
    lst=[]
    n=nums.copy()
    count=0
    for i in range(len(n)):
        if n[i] in lst:
            c=n.pop(i)
            print(f"removed form nums is {c}")
            print(f"the copied lst is {n}")

        else :
            lst.append(n[i])
            while len(nums)<=len(lst):
                nums[i]=lst[i]
            print(f"for the length {lst}")
            print(f"the copied lst is {n}")
    return len(lst)
nums=[0,0,1,1,2,3,4,4,5,5]
removeDuplicates(nums)