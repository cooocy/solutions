# 15. 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
#
# 输入：nums = []
# 输出：[]
# 示例 3：
#
# 输入：nums = [0]
# 输出：[]
#  
#
# 提示：
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = list()
        nums.sort()
        i = 0
        while nums[i] <= 0 and i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # a a a b
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                if sum < 0:
                    left += 1
                if sum > 0:
                    right -= 1
            i += 1
        return result


if __name__ == '__main__':
    # -4, -1, -1, 0, 1, 2
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    # nums = [0, 0, 0]
    print(Solution().threeSum(nums))
