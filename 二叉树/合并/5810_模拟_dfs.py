#https://leetcode-cn.com/problems/merge-bsts-to-create-single-bst/solution/python-ha-xi-biao-cun-chu-xie-jie-dian-d-znft/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        n = len(trees)
        #通过哈希表存储叶结点
        leaf = {}
        for tree in trees:
            if tree.left:
                leaf[tree.left.val] = [tree,"L",False]
            if tree.right:
                leaf[tree.right.val] = [tree,"R",False]
        
        for i in range(n-1,-1,-1):
            tree = trees[i]
            if tree.val in leaf:
                tree_obj = leaf[tree.val]
                tree0 = tree_obj[0]
                ctr = tree_obj[1]
                if ctr == "L":
                    tree0.left = tree
                else:
                    tree0.right = tree
                del trees[i]
        if len(trees) == 1:
            self.flag = True
            #dfs检查树的有效性
            def dfs(node,l,r):
                if node.val <= l or node.val >= r:
                    self.flag = False
                    return
                if node.left:
                    #标记左叶节点访问
                    leaf[node.left.val][2] = True
                    dfs(node.left,l,min(r,node.val))
                if node.right:
                    #标记右叶节点访问
                    leaf[node.right.val][2] = True
                    dfs(node.right,max(l,node.val),r)
            dfs(trees[0],-float("inf"),float("inf"))
            if self.flag:
                for le in leaf:
                    if not leaf[le][2]:
                        return None
                return trees[0]
        return None
