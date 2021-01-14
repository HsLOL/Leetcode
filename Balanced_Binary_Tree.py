# coding=utf-8
"""
采用自底向上的递归方式
自底向上递归的做法类似于后序遍历，
对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。
如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回-1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # 将新值与父节点进行比较
        if self.data:  # 非空
            if data < self.data:            # 新值较小，放左边
                if self.left is None:       # 若空，则新建插入节点
                    self.left = TreeNode(data)
                else:                       # 否则，递归往下查找
                    self.left.insert(data)
            elif data > self.data:          # 新值较大，放右边
                if self.right is None:      # 若空，则新建插入节点
                    self.right = TreeNode(data)
                else:                       # 否则，递归往下查找
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        # print(self.data, end='')
        print(self.data)
        if self.right:
            self.right.PrintTree()


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


# 用于单步调试代码
if __name__ == '__main__':
    lists = [3, 9, 20, 23, 35, 15, 7]
    for index, value in enumerate(lists):
        if index == 0:
            root = TreeNode(lists[index])
        else:
            root.insert(lists[index])

    root.PrintTree()
    s = Solution()
    bools = s.isBalanced(root)
    print(f'result:{bools}')
