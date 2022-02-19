def twosum(nums, target):
    dict = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in dict:
            return dict[comp], i
        else:
            dict[nums[i]] = i

print(twosum([2,7,11,15], 9))
 