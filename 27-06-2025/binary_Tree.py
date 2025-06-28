'''
what is a tree:
    a tree is a data structure similar to a linekd list but instead of each node pointing simply to next node in a linear fashion
    a tree is an example of non-linear data structure
    a tree structure is a way of representing hierarchical nature of a strcture in a graphical form

    the root node is the tree with no parents there can bee at most one root node in a tree(node A in the above example)
    an edge refers to the link from a parent to a child (all links in the figure)
    a node with no children is called a leaf node(e,j,k,h and i)

    the set of all nodes at a given depth is called the level of tree(b,c and d are the same level)
    the depth of a node is the length of the path from root to node (depth of G is 2, A--> C--> G)
    the height of a node is length of path from that node to the deepest node
    
    the height of a tree is the length is the length of the path from the root to the deepest node in the tree
    A rooted tree with only onne node (the root) has a height of zero
Binary tree:
    a generic tree with a most two child with at most two child nodes for each parent node is known as a binary tree
    a binary tree is made of nodes that constitute a left pointer, a right pointer and a data element. the root pointer is the topmost node in the tree
    the left and right pointers recursively point to small subtree on either side
    an empty is also a valid binary tree
    a formal definition is a binary tree is either empty (represented by a none pointer), or is made of a single node, where the left and right pointers(recursive definition ahead) each point to a binary tree
full binary tree:
    a binary tree in which every node has 0 or 2 children is termed as a full binary tree
complete binary tree:
    a complete binary tree has all the levels filled except for the last level which has all its nodes as much as to the left
perfect binary tree:
    a binary tree is termed perfect when all its internal node have two children along with the leaf nodes that are at same level
degebarted tree:
    in a degenerated tree, each internal node has only one child
balanced binary tree:
    a binary tree in which the differences between the depth of two subtrees of wvwey node is at most one is called a balanced binary tree
basic operations
    deleting an element from a tree
    searching for an element
    traversing the tree
auxillaru operations
    finding the size of tree
    finding the heght of the tree
    finding the level which has the maximum sum and many more..
traversals of binary tree
preorder -> root - left - right
post order -> left - right - root
inorder -> left - root - right
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binarytree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        else:
            queue = [self.root]
            while queue:
                temp = queue.pop(0)
                if not temp.left:
                    temp.left = new_node
                    return
                else:
                    queue.append(temp.left)
                if not temp.right:
                    temp.right = new_node
                    return
                else:
                    queue.append(temp.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

bt = Binarytree()
for val in [10, 5, 15, 3, 7, 12, 10]:
    bt.insert(val)

print("In order: ")
bt.inorder(bt.root)
print("\nPre order:")
bt.preorder(bt.root)
print("\nPost order:")
bt.postorder(bt.root)
print("\nLevel order:")
bt.level_order()