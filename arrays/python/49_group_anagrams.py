class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) 

        for string in strs:
            count = [0] * 26 # a-z char count of each string
            for char in string:
                count[ord(char) - ord('a')] += 1     
            # hashmapping char count to anagram group
            anagrams[tuple(count)].append(string)

        return anagrams.values()

# bad solution :(
class Solution:
    def tokenizeString(self, string):
        present_chars = {}

        for char in string:
            if char in present_chars:
                present_chars[char] += 1
            else:
                present_chars[char] = 1

        return present_chars

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        dicts = []

        for string in strs:
            string_dict = self.tokenizeString(string)
            if string_dict in dicts:
                group_index = dicts.index(string_dict)
                anagrams[group_index].append(string)
            else:
                dicts.append(string_dict)
                anagram_group = [string]
                anagrams.append(anagram_group)

        return anagrams
