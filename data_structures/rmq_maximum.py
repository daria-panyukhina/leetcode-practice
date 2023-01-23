class Solution:
    def maxSlidingWindow(self, nums, k):
        st = self.create_sparse_table(nums)
        res = []
        q = 0
        while 2 ** (q + 1) < k:
            q += 1
        for i in range(len(nums) - (k - 1)):
            j = i + k
            max1 = st[q][i]
            max2 = st[q][j - 2 ** q]
            res.append(max(max1, max2))
        return res

    def create_sparse_table(self, nums):
        sparse_table = [nums]
        k = 1
        dist = 2 ** k
        while dist < len(nums):
            sparse_table.append([])
            for i in range(len(nums) - k):
                if i + dist <= len(nums):
                    prev_dist1 = sparse_table[k - 1][i]
                    prev_dist2 = sparse_table[k - 1][i + dist // 2]
                    sparse_table[k].append(max(prev_dist1, prev_dist2))
            k += 1
            dist = 2 ** k
        return sparse_table

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
# print(s.create_sparse_table(nums))
print(s.maxSlidingWindow(nums, 3))
