class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return len(s) 
        
        longest_substring: str = ''
        for i in range(len(s)):
            current_substring: str = ''
            string_to_work_with = s[i::]
            if len(string_to_work_with) < len(longest_substring):
                break
            for ch in string_to_work_with:
                if ch in current_substring:
                    break
                current_substring = current_substring + ch
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        return len(longest_substring)