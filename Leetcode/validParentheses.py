class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'}': '{', ']': '[', ')': '('}

        for x in s:
            print(x)
            if x in '([{':
                stack.append(x)
            else:
                if stack and d[x] != stack[-1]:
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    sol.isValid("()[]{}")
