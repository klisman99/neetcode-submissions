class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for i in range(len(s)):
            c = s[i]

            if c in pairs.keys():
                stack.append(c)
            else:
                if not stack or pairs.get(stack.pop()) != c:
                    return False
        
        return not stack