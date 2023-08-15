class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        # remember self.head is not defined

    def print_List(self):
        curr = self.head
        while curr.next is not None:
            print(curr.data)
            curr = curr.next
        print(curr.data)

    def append(self, data):
        # insertion at end
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        self.count += 1

    def prepend(self, data):
        # insertion at start
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert(self, d, val):
        new_node = Node(d)
        index_node = self.head

        while index_node.data != val:
            index_node = index_node.next

        new_node.next = index_node.next
        index_node.next = new_node

    def swapnodes(self, n1, n2):
        if n1 > n2:
            temp = n2; n2 = n1; n1 = temp
        if n1 == n2 :
            return

        node1 = None ; node2 = self.head ; i = 1
        while i != n1:
            i += 1
            node2 = node2.next
        node1 = node2
        while i != n2 :
            i += 1
            node2 = node2.next

        temp = node1.data
        node1.data = node2.data
        node2.data = temp
