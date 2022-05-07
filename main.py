from nodelist import Node, LinkedList

# Singly Linked List with insertion and print methods
# l1 = Node(1, 0)
# l2 = Node(2, 0)

# l1_first = Node(8)
# l1_second = Node(1, l1_first)
# l1_third = Node(2, l1_second)
#
# l2_first = Node(5)
# l2_second = Node(6, l2_first)
# l2_third = Node(4, l2_second)

l1 = LinkedList()
l1.insert(3)
l1.insert(2)
l1.insert(1)

l2 = LinkedList()
l2.insert(5)
l2.insert(6)
l2.insert(8)


class Solution:
    @staticmethod
    def add_two_numbers(first_ll, second_ll):

        dummy = cur = Node(0)
        carry = 0

        while first_ll or second_ll or carry:
            if first_ll:
                carry += first_ll.val
                first_ll = first_ll.next
            if second_ll:
                carry += second_ll.val
                second_ll = second_ll.next

            cur.next = Node(carry % 10)
            cur = cur.next
            carry //= 10

        return dummy.next

    # print method for the linked list
    def print_ll(self, nodelist1, nodelist2):
        node = self.add_two_numbers(nodelist1, nodelist2)
        while node:
            print(node.val, end='')
            node = node.next


s = Solution().print_ll(l1.head, l2.head)
