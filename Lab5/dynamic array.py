def getConcatenation( nums):
    ans = []
    # ans=nums.copy()
    # ans.extend(nums)
    # return ans
    # for i in range(len(nums)):
    # ans[2 * len(nums) - i] = nums[2 * len(nums) - i]
    # for j in range(2):
    #     for i in range(len(nums)):
    #         ans.append(nums[i])
    for j in range(2):
        ans=ans+nums
    return ans
x=getConcatenation([1,2,3,4])
print(x)
