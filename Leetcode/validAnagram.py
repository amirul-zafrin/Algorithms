from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ch in t:
            if ch not in s:
                return False
            s = s.replace(ch, "", 1)
        if s:
            return False
        else:
            return True

    def betterApproach(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    print(sol.betterApproach("anagram", "nagaram"))
