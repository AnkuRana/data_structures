from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.current_node = None

    def add_node(self, value):
        """add node to the end of the linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.current_node = self.head
            return
        self.current_node.next = new_node
        self.current_node = new_node

    def add_node_at_start(self, value):
        """add node to the beginning of the linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        """print complete linked list"""
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            temp_node = self.head
            while temp_node is not None:
                print(temp_node.value, end="-->")
                temp_node = temp_node.next

    def insert(self, position, value):
        """insert a node at the given position. Take 1 as position of head"""
        count = 1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif position == 1:
            self.add_node_at_start(value)
        else:
            temp_node = self.head
            while temp_node is not None:
                prev_node = temp_node
                temp_node = temp_node.next
                count += 1
                if count == position:
                    new_node.next = temp_node
                    prev_node.next = new_node



