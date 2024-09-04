class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ''.join(char for char in s if char.isalnum()).lower()
        string_len = len(clean_string)

        for index in range(0, string_len):
            if clean_string[index] != clean_string[string_len-index-1]:
                return False

        return True
