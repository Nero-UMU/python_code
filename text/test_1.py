class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag = strs[0]
        for i in range(1, len(strs)):
            for each in strs:
                if each[:i+1] == flag[:i+1]:
                    pass
                else:
                    break


if __name__ == '__main__':
    f = Solution
    f.longestCommonPrefix(["flower", "flow", "flight"])