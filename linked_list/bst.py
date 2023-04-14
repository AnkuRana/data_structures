class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        new_node = Node(new_val)
        if self.root is None:
            self.root = new_node 
            return
        prev = None
        temp = self.root
        while temp is not None:
            if temp.value >= new_val:
                if temp.left is None:
                    temp.left =  new_node
                    break
                temp = temp.left     
            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
                
            # if prev.value >= new_val:
            #     prev.left = new_node
            # else:
            #     prev.right = new_node

    def search(self, find_val):
        if self.root is None:
            return None
        else:
            temp = self.root
            while temp is not None:
                if temp.value == find_val:
                    return True
                elif temp.value > find_val:
                    temp = temp.left
                else:
                    temp = temp.right
        return False
    
    def inorder(self, node):
        if node is None:
            return None
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
    
    def printAllBoundary(self):
        if self.root is None:
            return None
        self.printLeftBoundary(self.root)
        print(self.root.value, end=" ")
        self.printRightBoundary(self.root)
    
    def printLeftBoundary(self, node):
        if node is None:
            return
        self.printLeftBoundary(node.left)
        if node is not self.root:
            print(node.value, end= " ")
        
    def printRightBoundary(self, node):
        if node is None:
            return
        if node is not self.root:
            print(node.value, end=" ")
        self.printRightBoundary(node.right)
        
            
        
         
    
# Set up tree
tree = BST(12)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(18)
tree.insert(10)
tree.insert(5)
tree.insert(9)
tree.insert(14)

tree.inorder(tree.root)
print()
tree.printAllBoundary()
# Check search
# Should be True
print(tree.search(1))
# # Should be False
# print(tree.search(6))