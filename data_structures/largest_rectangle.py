class Solution:
    def largestRectangleArea(self, heights):
        st = self.create_sparse_table(heights)
        return self.find_max_square(0, len(heights), st, heights)

    def find_max_square(self, i, j, st, heights):
        if j <= i:
            return 0
        pivot = self.find_RMQ(i, j, st, heights)
        s1 = heights[pivot] * (j - i)
        s2 = self.find_max_square(i, pivot, st, heights)
        s3 = self.find_max_square(pivot + 1, j, st, heights)
        return max(s1, s2, s3)

    def find_RMQ(self, i, j, st, nums):
        q = 0
        while 2 ** (q + 1) < (j - i):
            q += 1
        idx1 = st[q][i]
        idx2 = st[q][j - 2 ** q]
        val1 = nums[idx1]
        val2 = nums[idx2]
        return idx1 if val1 < val2 else idx2

    def create_sparse_table(self, nums):
        sparse_table = [[i for i in range(len(nums))]]
        k = 1
        dist = 2 ** k
        while dist < len(nums):
            sparse_table.append([])
            for i in range(len(nums) - k):
                if i + dist <= len(nums):
                    prev_idx1 = sparse_table[k - 1][i]
                    prev_idx2 = sparse_table[k - 1][i + dist // 2]
                    prev_dist1 = nums[prev_idx1]
                    prev_dist2 = nums[prev_idx2]
                    sparse_table[k].append(prev_idx1 if prev_dist1 < prev_dist2 else prev_idx2)
            k += 1
            dist = 2 ** k
        return sparse_table

# class Solution:
#     def largestRectangleArea(self, heights):
#         stack = [-1]
#         max_area = 0
#         for i in range(len(heights)):
#             while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
#                 current_height = heights[stack.pop()]
#                 current_width = i - stack[-1] - 1
#                 max_area = max(max_area, current_height * current_width)
#             stack.append(i)
#
#         while stack[-1] != -1:
#             current_height = heights[stack.pop()]
#             current_width = len(heights) - stack[-1] - 1
#             max_area = max(max_area, current_height * current_width)
#         return max_area

nums = [2, 1, 5, 6, 2, 3]
s = Solution()
print(s.largestRectangleArea(nums))
# st = s.create_sparse_table(nums)
# print(s.find_RMQ(0, 6, st))
