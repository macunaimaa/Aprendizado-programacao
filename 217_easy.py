def containsDuplicate( nums: list[int]) -> bool:
    n = len(nums)
    flag = False
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            flag =  True
        else:
            continue
    return flag
            
array = [1,2,3,4]

solution = containsDuplicate(array)
print(solution)