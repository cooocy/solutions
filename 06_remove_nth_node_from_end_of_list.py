# 19. 删除链表的倒数第 N 个结点
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#  
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
#
# 提示：
#
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#  
#
# 进阶：你能尝试使用一趟扫描实现吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        维护一个 宽度为 n + 1 的滑动视窗, 用来保存最后的 n + 1 个 node.
        原始链表: A -> B -> C -> D -> E -> F -> G
        n = 3
        N: Null
        A, N, N, N
        A, B, N, N
        A, B, C, N
        A, B, C, D
        E, B, C, D
        E, F, C, D
        E, F, G, D
        """
        # idx 最后会等于 node 数量
        idx = 0
        array_len = n + 1
        mod = 0  # 从 mod + 1 开始读取, 即为最后 n + 1 个 node
        array = [None] * array_len
        cursor = head
        while cursor is not None:
            mod = idx % array_len
            array[mod] = cursor
            cursor = cursor.next
            idx += 1

        if idx < n:
            return head
        # node 数量 == n, 直接去掉头节点
        if idx == n:
            return head.next

        # idx > n
        idx_a = mod + 1

        # 假设: idx_a -> last_n -> idx_b
        # 找到 idx_a 和 idx_b 即可

        # 回到数组的头部
        if idx_a >= array_len:
            idx_a -= array_len
        idx_b = idx_a + 2
        if idx_b >= array_len:
            idx_b -= array_len
        if idx_a == idx_b:
            array[idx_a].next = None
        else:
            array[idx_a].next = array[idx_b]
        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, None)))))))
    # head = ListNode(1, ListNode(2))
    # head = ListNode(1)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = Solution().removeNthFromEnd(head, 2)
    print(result)
