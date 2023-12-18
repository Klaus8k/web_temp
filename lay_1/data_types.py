s = "a"
t = "a"

# попробовать сделать сет из второго и сравнить с количеством ключей первого
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_letter = {i: s.count(i) for i in s}
        for i in dict_letter.keys():
            if dict_letter[i] == t.count(i):
                continue
            else:
                return False
        return True






# Solution().isAnagram(s, t)
assert Solution().isAnagram(s, t) == 1, 'no annagramm'
