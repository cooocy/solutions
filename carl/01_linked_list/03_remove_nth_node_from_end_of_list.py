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

from kits.list_kits import ListNode, load_list, compare_list


class Solution:
    """
    可使用快慢指针和滑动窗口.
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        快慢指针.
        1. 先设置一个 dummy 节点.
        2. slow, fast 同时从 dump 开始.
        3. 先让 fast 移动 n 次, 之前 slow 和 fast 一起移动, fast = None, 停止.
        4. slow.next = slow.next.next
        """
        dummy = ListNode(0, head)
        slow, fast, i = dummy, dummy, 0
        while fast is not None:
            if i > n:
                slow = slow.next
            else:
                i += 1
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
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
    case = (
        (load_list([1, 2]), 2, load_list([2])),
        (load_list([1]), 1, load_list([])),
        (load_list([1, 2]), 1, load_list([1])),
        (load_list([1, 2, 3, 4, 5]), 2, load_list([1, 2, 3, 5])),
    )
    solution = Solution()
    for c in case:
        assert compare_list(solution.removeNthFromEnd(c[0], c[1]), c[2])

    case = (
        (load_list([1, 2]), 2, load_list([2])),
        (load_list([1]), 1, load_list([])),
        (load_list([1, 2]), 1, load_list([1])),
        (load_list([1, 2, 3, 4, 5]), 2, load_list([1, 2, 3, 5])),
    )
    solution = Solution()
    for c in case:
        assert compare_list(solution.removeNthFromEnd_2(c[0], c[1]), c[2])
