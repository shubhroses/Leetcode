from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_successor(root, key):
    q = deque([root])
    flag = False
    while q:
        for _ in range(len(q)):
            top = q.popleft()
            if flag:
                return top
            if top.val == key:
                flag = True
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
    return None

def main():
    root = TreeNode (12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)

if __name__ == "__main__":
    main()
