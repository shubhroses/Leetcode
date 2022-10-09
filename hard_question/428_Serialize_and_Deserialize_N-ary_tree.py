"""
Need to keep the problem stateless

Use an index to iterate over the data in the input string during deseralization. 
The nested class is simply to providd us iwth an iterator during our recursive calls
"""
class WrappableInt:
        def __init__(self, x):
            self.value = x
        def getValue(self):
            return self.value
        def increment(self):
            self.value += 1

class Codec:
    
    def serialize(self, root: 'Node') -> str:
        serializedList = []
        
        def _serializeHelper(root, identity, parentId):
            if not root:
                return
            # Own identity
            serializedList.append(chr(identity.getValue() + 48))
            # Actual value
            serializedList.append(chr(root.val + 48))
            # Parent's identity
            serializedList.append(chr(parentId + 48) if parentId else 'N')

            parentId = identity.getValue()
            for child in root.children:
                identity.increment()
                _serializeHelper(child, identity, parentId)
        
        _serializeHelper(root, WrappableInt(1), None)
        return "".join(serializedList)
    

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None

        nodesAndParents = {}
        for i in range(0, len(data), 3):
            identity = ord(data[i]) - 48
            orgValue = ord(data[i + 1]) - 48
            parentId = ord(data[i + 2]) - 48
            nodesAndParents[identity] = (parentId, Node(orgValue, []))

        for i in range(3, len(data), 3):

            # Current node
            identity = ord(data[i]) - 48
            node = nodesAndParents[identity][1]

            # Parent node
            parentId = ord(data[i + 2]) - 48
            parentNode = nodesAndParents[parentId][1]

            # Attach!
            parentNode.children.append(node)

        return nodesAndParents[ord(data[0]) - 48][1] 