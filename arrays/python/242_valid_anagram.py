class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        present_characters = {}

        for char in s:
            if char in present_characters:
                present_characters[char] += 1
            else:
                present_characters[char] = 1

        for char in t:
            if char in present_characters:
                present_characters[char] -= 1
                if present_characters[char] == 0:
                    present_characters.pop(char)
            else:
                return False

        if present_characters != {}:
            return False
        return True
