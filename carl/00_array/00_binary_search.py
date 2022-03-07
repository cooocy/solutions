# https://leetcode-cn.com/problems/binary-search/
# 704. 二分查找
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#
#
# 提示：
#
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。

from typing import List


class Solution:
    """
        https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md
        关于两个算法 区间条件 的说明:
        1. search_1() 的 while 条件是 [left, right], 所以调整边界时不需要考虑当前 middle, 取 middle + 1 或 middle - 1 即可.
        2. search_2() 的 while 条件是 [left, right), 所以调整边界时, left = middle + 1, right = middle.
    """

    def search_1(self, nums: List[int], target: int) -> int:
        # [left, right] 左闭右闭
        left, right = 0, len(nums) - 1
        while left <= right:
            # // 运算表示除法并向下取整. e.g. 5 // 2 = 2
            middle = (left + right) // 2
            if nums[middle] > target:
                # 因为 left 和 right 都是闭合的, right 取 middle - 1
                # [left, right_0] -> [left, right_1]
                right = middle - 1
            elif nums[middle] < target:
                # 因为 left 和 right 都是闭合的, left 取 middle + 1
                left = middle + 1
            else:
                return middle
        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        # [left, right) 左闭右开
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                # [left, right) right 取 middle
                right = middle
            elif nums[middle] < target:
                # [left, right) left 取 middle - 1
                left = middle + 1
            else:
                return middle
        return -1


if __name__ == '__main__':
    case = (
        # array, target expected
        ([0, 1, 2], 100, -1),
        ([0, 1, 2, 3, 4], 100, -1),
        ([0], 0, 0),
        ([-10, -5, 0, 2, 10], 10, 4)
    )
    solution = Solution()
    for c in case:
        assert solution.search_1(c[0], c[1]) == c[2]
        assert solution.search_2(c[0], c[1]) == c[2]
