class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            complemento = target - nums[i]
            if complemento in numMap and numMap[complemento] != 1:
                return i, numMap[complemento]                
solution =  Solution()

array = [0,1,2,3,4,5,6,7,8]
target = 9

idx1, idex2 =  solution.twoSum(array, target)
print(idx1, idex2)