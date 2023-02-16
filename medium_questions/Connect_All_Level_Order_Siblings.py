from __future__ import print_function
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next= None, None, None

    # tree traversal using 'next pointer
    def print_tree(self):
        print("Traversal using 'next' pointer; ", end="")
        current = self
        while current:
            print(str(current.val) + " ", end="")
            current = current.next

def connect_all_siblings(root):
    # TODO: Write your code here
    q = deque([root])
    prev = None
    while q:
        for _ in range(len(q)):
            top = q.popleft()
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
            if prev:
                prev.next = top
            prev = top
    prev.next = None


def main () :
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()

if __name__ == "__main__":
    main()