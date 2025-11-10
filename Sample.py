# BFS-2

## Problem 1

# Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)

# Traverse each level using a queue, collecting all node values in temp
# Take the last element of each level (temp[-1]) as it represents the rightmost visible node
# Handle null nodes by checking if curr before processing
# The rightmost node at each level is simply the last node processed in that level's BFS iteration. 
# This pattern works for any "view" problem (left/right/top/bottom) by adjusting which node you pick per level

# Time Complexity: O(N) — visit every node once
# Space Complexity: O(W) — maximum width of tree (queue stores one level at a time)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        while q:
            temp = []
            for i in range(len(q)):
                curr = q.pop(0)
                if curr:
                    temp.append(curr.val)
                
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
            if len(temp) > 0:
                last_ele = temp[-1]
                res.append(last_ele)
        return res


## Problem 2

# Cousins in binary tree (https://leetcode.com/problems/cousins-in-binary-tree/)

# Cousins in Binary Tree using BFS level-order traversal with these key checks:

# Same parent check: For each node, if it has both left/right children, verify they aren't (x,y) or (y,x) (would make them siblings, not cousins)
# Level-wise search: Track if x and y are found in the same level (x_found and y_found both true → return True)
# Early termination: If only one is found in a level (x_found XOR y_found), they can't be cousins → return False
# Cousins must be on the same depth but have different parents. BFS naturally processes nodes level-by-level, making it perfect for this problem
# Time Complexity: O(N) — visit each node once
# Space Complexity: O(W) — max width of tree (queue size)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        q = deque()
        q.append(root)
        x_found = False
        y_found = False

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left and curr.right:
                    if curr.left.val == x and curr.right.val == y:
                        return False
                    if curr.left.val == y and curr.right.val == x:
                        return False
                
                if curr.val == x:
                    x_found = True
                if curr.val == y:
                    y_found = True

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False
            

        


