# Definition for a binary tree node.
# coding=utf-8


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

    # 打印这棵树，中序遍历
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        # print(self.data, end='')
        print(self.data)
        if self.right:
            self.right.PrintTree()


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:  # -> int 代表函数返回值的注释，此题代表返回int
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.data
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


if __name__ == '__main__':

    # 建树
    lists = [15, 10, 20, 8, 12, 17, 25]
    for index, _ in enumerate(lists):
        if index == 0:
            root = TreeNode(lists[index])
        else:
            root.insert(lists[index])

    # 找k大值
    tool = Solution()
    result = tool.kthLargest(root, k=2)
    print(result)
