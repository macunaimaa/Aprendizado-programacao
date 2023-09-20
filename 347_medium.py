class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mp = {}
        lis = []
        res = []
        
        for num in nums:
            if num in mp:
                mp[num] += 1  # Increment the frequency count for the number
            else:
                mp[num] = 1   # Initialize the frequency count for the number
        
        # Creating a list of frequency-number pairs and sorting it in reverse order
        sorted_freq_pairs = sorted(mp.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            res.append(sorted_freq_pairs[i][0])  # Appending the 'k' most frequent numbers to the result
        
        return res

solution = Solution()

nums = [4,4,4,4,4,4,4,4,4,4,1, 1, 1, 2, 2, 3,12,12,12,13,13,13,13,14,14,14,14,14,14,14]
k =4

resultado = solution.topKFrequent(nums, k)

print(resultado)
