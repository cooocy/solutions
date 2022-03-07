# 209. 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
#
#
# 示例 1：
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：
#
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#
#
# 提示：
#
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
#
#
# 进阶：
#
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        两种解法:
        1. 两层循环, N * N
        2. 快慢指针, 是一种滑动窗口.
        - a. 两个指针都从 0 开始.
        - b. 快指针往后, 当 区间总和大于等于目标值, 记录此区间长度, 并将慢指针右移, 直到不满足总和, 最后一次的快慢差即为当前终点的最短序列.
        - c. 快指针继续移动.
        """

        # sub_len 无限大
        slow, fast, sub_sum, sub_len = 0, 0, 0, float('inf')
        for fast in range(len(nums)):
            sub_sum += nums[fast]
            while sub_sum >= target:
                sub_len = min(fast - slow + 1, sub_len)
                sub_sum -= nums[slow]
                slow += 1
        if sub_len == float('inf'):
            return 0
        else:
            return sub_len


if __name__ == '__main__':
    case = (
        ([2, 3, 1, 2, 4, 3], 7, 2),
    )
    solution = Solution()
    for c in case:
        assert solution.minSubArrayLen(c[1], c[0]) == c[2]
