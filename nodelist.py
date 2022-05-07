# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, val):
        new_node = Node(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    # method to reverse the list
    def reverse(self, head):

        if head is None or head.next is None:
            return head

        rest = self.reverse(head.next)

        head.next.next = head
        head.next = None

        return rest

    # print method for the linked list
    def print_ll(self):
        current = self.head
        while current:
            print(current.val, end='')
            current = current.next
