from nodelist import Node, LinkedList


class Solution:
    @staticmethod
    def add_two_numbers(first_ll: Node, second_ll: Node) -> Node:
        """
        :param first_ll: Node
        :param second_ll: Node
        :return: Node
        """
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

    # converts the nodelist to a number
    def nodelist_to_number(self, nodelist1, nodelist2):
        node = self.add_two_numbers(nodelist1, nodelist2)
        result = ""
        while node:
            result += str(node.val)
            node = node.next
        return int(result)

# l1 = LinkedList()
# l1.insert(3)
# l1.insert(2)
# l1.insert(1)
#
# l2 = LinkedList()
# l2.insert(5)
# l2.insert(6)
# l2.insert(8)
#
# print(Solution().nodelist_to_number(l1.head, l2.head))
