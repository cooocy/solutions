# 024. 反转链表
# 给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：[2,1]
# 示例 3：
#
# 输入：head = []
# 输出：[]
#  
#
# 提示：
#
# 链表中节点的数目范围是 [0, 5000]
# -5000 <= Node.val <= 5000
#  
#
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/UHnkqh
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # a > b > c > d > e
        n1, n2, n3 = head, head.next, None
        while n2 is not None:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        head.next = None
        return n1


if __name__ == '__main__':
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    n = Solution().reverseList(node)
