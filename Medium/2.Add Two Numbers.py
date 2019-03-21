class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        res_node = ListNode(None)
        res = res_node
        remainder = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            res.next = ListNode((num1+num2+remainder) % 10)
            remainder = (num1+num2+remainder) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next
        if remainder != 0:
            res.next = ListNode(remainder)
        return res_node.next


l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(9)
l1.next = l2
l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

s = Solution().addTwoNumbers(l1, l4)
while s:
    print(s.val)
    s = s.next
