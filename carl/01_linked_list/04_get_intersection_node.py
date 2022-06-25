# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
#
# 图示两个链表在节点 c1 开始相交：
#
#
#
# 题目数据 保证 整个链式结构中不存在环。
#
# 注意，函数返回结果后，链表必须 保持其原始结构 。
#
#  
#
# 示例 1：
#
#
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 示例 2：
#
#
#
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Intersected at '2'
# 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
# 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
# 示例 3：
#
#
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
# 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 这两个链表不相交，因此返回 null 。
#  
#
# 提示：
#
# listA 中节点数目为 m
# listB 中节点数目为 n
# 0 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA <= m
# 0 <= skipB <= n
# 如果 listA 和 listB 没有交点，intersectVal 为 0
# 如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]
#  
#
# 进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/

from kits.list_kits import ListNode, load_list, compare_list


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        1. 相交的两个链表, 尾结点一定相等.
        2. 首先要判断链表是否相交.
        3. 假设有链表 a(1,2,3,4), 链表 b(1,3,4)
           a 和 b 相交于 3;
           len(a) = 4, len(b) = 3
           a 比 b 长 1, 则逐个比较 a(n + 1) 和 b(n) 直至相等.
        """
        if headA is None or headB is None:
            return None

        a = headA
        b = headB

        # 定位到两个链表的尾结点, 并计算链表长度.
        len_a = 1
        while headA.next is not None:
            headA = headA.next
            len_a += 1
        len_b = 1
        while headB.next is not None:
            headB = headB.next
            len_b += 1

        # 如果尾结点不等, 不相交
        if headA != headB:
            return None

        # a: □ □ □ □ ■ ■
        # b:       □ ■ ■
        # 将 a 的初始指针定位到和 b 一样长的位置. 即 a(3)
        diff = len_a - len_b
        if diff >= 0:
            idx = 0
            while idx < diff:
                a = a.next
                idx += 1
        else:
            idx = 0
            while idx < 0 - diff:
                b = b.next
                idx += 1

        while a != b:
            a = a.next
            b = b.next

        return a
