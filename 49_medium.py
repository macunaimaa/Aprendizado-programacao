class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in map:
                map[sorted_word].append(word)
            else:
                map[sorted_word] = [word]

        return list(map.values())

solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(strs)
print(result)