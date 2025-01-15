# Solution to problem Existence_of_a_Substring_in_a_String_and_Its_Reverse
# Problem ID: 3083

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            leng = 0
            for j in range(len(s) - 1, 0, -1):
                if s[i] == s[j] and s[i+1] == s[j-1]:
                    return True
        return False
