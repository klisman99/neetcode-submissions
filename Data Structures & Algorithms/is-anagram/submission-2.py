class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}
        chars_t = {}

        for i in range(len(s)):
            chars_s[s[i]] = chars_s.get(s[i], 0) + 1

        for i in range(len(t)):
            chars_t[t[i]] = chars_t.get(t[i], 0) + 1

        for key, value in chars_s.items():
            if key not in chars_t:
                return False

            if chars_t.get(key) != value:
                return False
        
        for key, value in chars_t.items():
            if key not in chars_s:
                return False

            if chars_s.get(key) != value:
                return False

        return True