class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return len(s) 
        
        max_substring_length = 0
        current_substring = ''
        for ch in s:
            if ch in current_substring:
                current_substring = current_substring[current_substring.index(ch)+1::]
                print(current_substring, len(current_substring))
            current_substring = current_substring + ch
            if len(current_substring) > max_substring_length:
                    max_substring_length = len(current_substring)
        return max_substring_length
 