from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def load_list(array: List[int]) -> Optional[ListNode]:
    head, cursor = None, None
    for idx in range(len(array)):
        if idx == 0:
            head = ListNode(array[idx])
            cursor = head
        if idx < len(array) - 1:
            cursor.next = ListNode(array[idx + 1])
            cursor = cursor.next
    return head


def compare_list(a: ListNode, b: ListNode):
    cursor_a: ListNode = a
    cursor_b: ListNode = b
    while True:
        if cursor_a is None and cursor_b is None:
            return True
        if (cursor_a is None) ^ (cursor_b is None):
            return False
        if cursor_a.val != cursor_b.val:
            return False
        cursor_a = cursor_a.next
        cursor_b = cursor_b.next
    return True
