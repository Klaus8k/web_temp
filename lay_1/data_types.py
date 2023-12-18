s = "angagram"
t = "nagarasm"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_letter = {i: s.count(i) for i in s}
        for i in dict_letter.keys():
            if dict_letter[i] == t.count(i):
                continue
            else:
                return False
        return True






# Solution().isAnagram(s, t)
assert Solution().isAnagram(s, t) == 1, 'no annagramm'
