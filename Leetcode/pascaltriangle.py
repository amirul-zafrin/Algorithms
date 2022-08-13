class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]*(n+1) for n in range(numRows)]
        if numRows < 2:
            return res

        for k in range(2, numRows):
            for i in range(1, len(res[k]) - 1):
                res[k][i] = (res[k-1][i] + res[k-1][i-1])

        return res


if __name__ == "__main__":
    sol = Solution()
    sol.generate(5)
