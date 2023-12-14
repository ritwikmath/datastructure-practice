class Solution:
    def longestCommonPrefix(self, strs) -> str:
        sorted_strs = sorted(strs)
        key = 0
        prefix = ''
        while True:
            try:
                if sorted_strs[0][key] == sorted_strs[-1][key]:
                    prefix += sorted_strs[0][key]
                else:
                    break
            except IndexError:
                break
            key += 1
        return prefix
