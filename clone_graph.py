# Given a node in a connected undirected graph, return a deep copy of the graph.

# Each node in the graph contains an integer value and a list of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

# The input node will always be the first node in the graph and have 1 as the value.

# Input: 
adjList = [[2],[1,3],[2]]

# Output: [[2],[1,3],[2]]
# Explanation: There are 3 nodes in the graph.
# Node 1: val = 1 and neighbors = [2].
# Node 2: val = 2 and neighbors = [1, 3].
# Node 3: val = 3 and neighbors = [2].

# Example 2:



# Input: adjList = [[]]

# Output: [[]]
# Explanation: The graph has one node with no neighbors.

# Example 3:
# Input: adjList = []
# Output: []

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
            


        

if __name__=='__main__':
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2,n4]
    n2.neighbors = [n1,n3]
    n3.neighbors = [n2,n4]
    n4.neighbors = [n1,n3]
    s = Solution()
    out = []
    for item in [n1,n2,n3,n4]:
        nd = s.cloneGraph(item)
        out.append([n.val for n in nd.neighbors])
    print(out)

   


