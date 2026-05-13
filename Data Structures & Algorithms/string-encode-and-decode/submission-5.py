class Solution:
    DELIMITER = "__&__"

    def encode(self, strs: list[str]) -> str:
        buffer = ""

        if len(strs) == 0: return ""

        for str in strs:
            buffer += self.DELIMITER + str

        return buffer

    def decode(self, s: str) -> list[str]:
        if s == "": return []

        res = []

        for i, value in enumerate(s.split(self.DELIMITER)):
            if i == 0: continue

            res.append(value)

        return res