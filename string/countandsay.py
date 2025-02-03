class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = "" + self.countAndSay(n-1)

        encoded_string = ""
        previous = ""
        count = 1
        length_of_string = len(result)
        for i in range(length_of_string):
            if previous == result[i]:
                count += 1
            elif previous not in [result[i], ""]:
                encoded_string += f"{count}{previous or result[i]}"
                count = 1
            
            if i == (length_of_string - 1):
                encoded_string += f"{count}{result[i]}"

            previous = result[i]

        return encoded_string

if __name__ == "__main__":
    result = Solution().countAndSay(2)
    print(result)