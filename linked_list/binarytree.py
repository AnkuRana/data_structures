class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
        


    def pre_order(self, node):
        if node is None:
            return
        print(f"{node.value}", end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)
    
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(f"{node.value}", end=" ")
        self.in_order(node.right)
 
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(f"{node.value}", end=" ")
        
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

b = BinaryTree()
print("Pre_order traversal:")
b.pre_order(root)
print()
print("In_order traversal:")
b.in_order(root)
print()
print("Post-ordder traversal:")
b.post_order(root)

            
            