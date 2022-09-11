class Solution:
    def toLowerCase(self, s: str) -> str:
        li = list(s)

        for i in range(len(s)):
            if ord(li[i]) > 64 and ord(li[i]) < 91:
                li[i] = chr(ord(li[i])+32)

        return ''.join(li)