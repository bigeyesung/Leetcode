class Solution:

    def maxDepth(self, root: 'Node') -> int:
        #Time: O(N)
        #Space:O(h): tree height
        def Dfs(node):
            if not node:
                return 0
            depth=0
            for ind in range(len(node.children)):
                depth=max(depth,Dfs(node.children[ind]))
            return depth+1
        return Dfs(root)
        
        #Time: O(N)
        #Space:O(N)
        def Bfs(node):
            if not node:
                return 0
            queue = [node]
            depth=0
            while(queue):
                count = len(queue)
                while(count!=0):
                    node=queue.pop(0)
                    for ind in range(len(node.children)):
                        queue.append(node.children[ind])
                    count-=1
                depth+=1
            return depth
        return Bfs(root)
