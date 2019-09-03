class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):
        dummy_head = ListNode(0)
        p = l1
        q = l2
        cur = dummy_head
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            r = x + y + carry
            carry = r // 10
            cur.next = ListNode(r % 10)
            cur = cur.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy_head.next


if __name__ == "__main__":
    n1 = ListNode(1)

    n4 = ListNode(9)
    n5 = ListNode(9)

    n4.next = n5
    link = Solution().add_two_numbers(n1, n4)
    print(link.val)
    print(link.next.val)
    print(link.next.next.val)
