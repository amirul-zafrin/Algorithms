class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while 1 < right:
            idx = (left+right) // 2
            if matrix[idx][0] > target:
                right = idx - 1
            elif matrix[idx][-1] < target:
                left = idx + 1
            else:
                left = idx
                break

        if not (matrix[left][0] <= target <= matrix[left][-1]):
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            i = (l+r)//2
            if matrix[left][i] > target:
                r = i - 1
            elif matrix[left][i] < target:
                l = i + 1
            else:
                return True

        return True


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13

    sol = Solution().searchMatrix(matrix, target)
    print(sol)
