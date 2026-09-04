class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list(strs[0])
        for i in strs:
            while prefix != list(i)[:len(prefix)]:
                prefix.pop()
        return ''.join(prefix)
        