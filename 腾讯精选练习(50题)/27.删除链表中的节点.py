class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, node):
        """
        :param node: ListNode
        :return: void
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
