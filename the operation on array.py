def applyOperations(nums):
    count = 0
    zero = []
    l = []
    for i in range(len(nums)):
        if i+1!= len(nums):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                print(nums)
                count += 1



    for i in nums:
        if i != 0:
            l.append(i)

        else:
            zero.append(0)
    return l+zero
n=[847,847,0,0,0,399,416,416,879,879,206,206,206,272]
print(applyOperations(n))