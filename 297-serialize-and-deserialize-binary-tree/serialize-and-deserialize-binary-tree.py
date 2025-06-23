class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def rserialize(node, stream):
            if not node:
                stream.append('None')
            else:
                stream.append(str(node.val))
                rserialize(node.left, stream)
                rserialize(node.right, stream)
        
        stream = []
        rserialize(root, stream)
        return ','.join(stream)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def rdeserialize(stream):
            val = next(stream)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = rdeserialize(stream)
            node.right = rdeserialize(stream)
            return node
        
        stream = iter(data.split(','))
        return rdeserialize(stream)