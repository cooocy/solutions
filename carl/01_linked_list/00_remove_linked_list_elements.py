# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 示例 2：
#
# 输入：head = [], val = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
#  
#
# 提示：
#
# 列表中的节点数目在范围 [0, 104] 内
# 1 <= Node.val <= 50
# 0 <= val <= 50
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-linked-list-elements
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from kits.list_kits import ListNode, load_list, compare_list


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        给原本的链表添加一个虚拟的头节点
        """
        dummy = ListNode(val - 1, head)
        cursor = dummy
        while cursor.next is not None:
            if cursor.next.val == val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        return dummy.next


if __name__ == '__main__':
    case = (
        (load_list([1, 1, 1, 1, 1]), 1, load_list([])),
        (load_list([1, 2, 3, 4]), 4, load_list([1, 2, 3])),
        (load_list([]), 4, load_list([])),
        (load_list([1, 2, 2, 2, 4]), 2, load_list([1, 4])),
        (load_list([1, 1, 2, 2, 1, 1]), 1, load_list([2, 2])),
    )
    solution = Solution()
    for c in case:
        assert compare_list(solution.removeElements(c[0], c[1]), c[2])
