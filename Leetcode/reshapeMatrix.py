class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:

        res = [[0]*c for i in range(r)]
        x = len(mat)
        y = len(mat[0])

        if x*y != r*c:
            return mat

        for i in range(x*y):
            res[i//c][i % c] = mat[i//y][i % y]

        return res


if __name__ == "__main__":
    sol = Solution()
    a = sol.matrixReshape([[1, 2], [3, 4]], 1, 4)
    print(a)
