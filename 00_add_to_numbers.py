# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 599: 9 -> 9 -> 5
# 987: 7 -> 8 -> 9
# 1586: 6 -> 8 -> 5 -> 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        first = None
        end = None
        while True:
            if l1 is None and l2 is None:
                if carry != 0:
                    end.next = ListNode(carry, None)
                break
            v1 = 0
            v2 = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next
            sum = v1 + v2 + carry
            if sum > 9:
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            if first is None:
                first = ListNode()
                end = first
            else:
                end.next = ListNode()
                end = end.next
            end.val = sum

        return first


if __name__ == '__main__':
    # l1 = ListNode(9, ListNode(9, ListNode(9, None)))
    # l2 = ListNode(9, None)
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    result = Solution().addTwoNumbers(l1, l2)
    print(result)
