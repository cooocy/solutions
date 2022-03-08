# 24. 两两交换链表中的节点
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
#
# 输入：head = []
# 输出：[]
# 示例 3：
#
# 输入：head = [1]
# 输出：[1]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/

from kits.list_kits import ListNode, load_list, compare_list


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev, pair_a, pair_b = dummy, dummy.next, None
        if pair_a is not None:
            pair_b = pair_a.next
        while pair_b is not None:
            pair_a.next = pair_b.next
            pair_b.next = pair_a
            prev.next = pair_b
            prev = pair_a
            pair_a = pair_a.next
            if pair_a is None:
                pair_b = None
            else:
                pair_b = pair_a.next
        return dummy.next


if __name__ == '__main__':
    case = (
        (load_list([]), load_list([])),
        (load_list([2, 1, 4, 3]), load_list([1, 2, 3, 4])),
    )
    solution = Solution()
    for c in case:
        assert compare_list(solution.swapPairs(c[0]), c[1])
