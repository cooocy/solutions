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
