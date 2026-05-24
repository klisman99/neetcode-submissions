"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        clones = {}

        def deepClone(node):
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(deepClone(neighbor))

            return copy

        return deepClone(node) if node else None
