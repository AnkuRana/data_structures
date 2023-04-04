class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_node(self, curr_node, value):
        if self.head is None:
            self.head = Node(value)   
        elif curr_node.next is None:
            curr_node.next = Node(value)
            return
        else:
            self.insert_node(curr_node.next, value)
 
    def reverseRec(self, node):
        if node.next is None:
            return node
        else:
            node_returned = self.reverseRec(node.next)
            node.next.next = node
            node.next = None
            return node_returned
        
                       
def print_ll(head):
        if head is None:
            print("Empty linked list.")
        else:
            temp = head
            while temp is not None:
                print(f"{temp.value}",end="->")
                temp = temp.next

def mergeSortedlinkedlists(head_1, head_2):
    if head_1 is None:
        return head_2
    if head_2 is None: 
        return head_1
    
    if head_1.value > head_2.value:
        head_2.next = mergeSortedlinkedlists(head_1, head_2.next)
        return head_2
    else:
        head_1.next = mergeSortedlinkedlists(head_1.next, head_2)
        return head_1
            
l1 = linkedlist()
l2 = linkedlist()
first = [1, 3, 7, 8, 9]
second = [2, 4, 5, 6, 10]
for i in range(len(first)):
    l1.insert_node(l1.head, first[i])
for i in range(len(second)):
    l2.insert_node(l2.head, second[i])
print("first linked list: ", end="")
print_ll(l1.head)
print()
print("second linked list: ", end="")
print_ll(l2.head)
print()
merge_head = mergeSortedlinkedlists(l1.head, l2.head)
print("Merged linked list: ", end="")
print_ll(merge_head)
print()
print("Reverse Merged linked list: ", end="")
new_head = l1.reverseRec(merge_head)
print_ll(new_head)

       
            
        