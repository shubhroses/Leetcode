# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #Perform a level order traveral if the binary tree which uses a queue
        """
        1. Create queue add root to it
        2. While queue pop from queue, add left and right to queue
        """
        if not root: return 'x'
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data
        if data[0] == 'x': return None
        node = TreeNode(self.data[:self.data.find(',')]) 
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])
        return node

    def serialize(self, root):
        
        def rserialize(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        return rserialize(root, "")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            if l[0] == "None":
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root
        data_list = data.split(",")
        root = rdeserialize(data_list)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))