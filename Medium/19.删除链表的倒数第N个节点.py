class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 解法1：两次遍历
    def remove_nth_from_end1(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0
        while first is not None:
            length += 1
            first = first.next
        length = length - n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

    # 解法2:一次遍历
    def remove_nth_from_end2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        last = dummy
        while n >= 0:
            first = first.next
            n -= 1
        while first is not None:
            first = first.next
            last = last.next
        last.next = last.next.next
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    h = Solution().remove_nth_from_end2(l1, 2)
    print(h.val)
    print(h.next.val)
    print(h.next.next.val)
    print(h.next.next.next.val)
