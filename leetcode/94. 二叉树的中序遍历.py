from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        result=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                currentNode=stack.pop()
                result.append(currentNode.val)
                root=currentNode.right
        return result

if __name__=="__main__":
    print(Solution().inorderTraversal([1,None,2,3]))