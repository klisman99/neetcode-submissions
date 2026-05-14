class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for i in range(len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])
            else:
                if not stack or pairs.get(stack.pop()) != s[i]:
                    return False
        
        return not stack