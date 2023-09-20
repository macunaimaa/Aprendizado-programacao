class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
    

s = "anagrama"
t = "aangrama"
solution = Solution()

retorno = solution.isAnagram(s,t)
print(retorno)