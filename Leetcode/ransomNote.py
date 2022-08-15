class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = 'abcdefghijklmnopqrstuvwxyz'

        note = {l: ransomNote.count(l)
                for l in letters if ransomNote.count(l) > 0}
        mg = {l: magazine.count(l) for l in letters if magazine.count(l) > 0}

        for k in note.keys():
            if not mg.get(k):
                return False
            elif note[k] > mg[k]:
                print(note[k] > mg[k])
                return False

        return True

    def betterApproach(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine = magazine.replace(ch, "", 1)
        return True


if __name__ == "__main__":
    sol = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(sol.canConstruct(ransomNote, magazine))
    ransomNote = "a"
    magazine = "b"
    print(sol.canConstruct(ransomNote, magazine))
