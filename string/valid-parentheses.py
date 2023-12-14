class Solution:
    def isValid(self, s):
        closing = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        next_close = []
        for ch in s:
            if ch in closing:
                next_close.append(closing[ch])
                continue

            if ch in next_close and ch == next_close[-1]:
                next_close.pop()
            else:
                return False 
        return not bool(next_close)
