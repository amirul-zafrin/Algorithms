import enum


class Solution:
    def firstUniqChar(self, s: str) -> int:

        d = {}
        for i in range(len(s)):
            # print(s[i])
            if d.get(s[i]) is None:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)

        for k, v in d.items():
            if len(v) == 1:
                return v[0]

        return -1

    def betterApproach(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


if __name__ == "__main__":
    sol = Solution()
    a = sol.firstUniqChar("leetcode")
    b = sol.firstUniqChar("aadadaad")
    print(a)
    print(b)
