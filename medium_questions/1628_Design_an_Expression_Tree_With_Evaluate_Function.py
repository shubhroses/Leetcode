import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode():
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        else:
            return self.left.evaluate() // self.right.evaluate()
        
        
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        cur = None
        for char in postfix:
            cur = TreeNode(char)
            if char in ['+', '-', '*', '/']:
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        for e in stack:
            print(e.val)
        return cur
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

"""
["3","4","+","2","*","7","/"]
  i

stack = []

          /
      *      7
   +     2
 3  4


["4","5","2","7","+","-","*"]
                      i

stack = [4 -]
  *
4     -
    5   +
       2 7
       
stack = [*]


 
"""

    
    