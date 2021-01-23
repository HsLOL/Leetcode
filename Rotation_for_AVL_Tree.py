# coding=utf-8


class AVLTreeNode(object):
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return "{ %d : left %s ; right %s }" % (self.key, self.left, self.right)


class Solution():

    @staticmethod
    def get_height(node):
        return node.height if node else -1

    def right_rotate(self, root, node):  # 右旋， 用于LL型失衡
        # 先将 node 和 node_left 之间及其左右节点赋值 (node_left.left node.right 保持不变)
        node_left = node.left
        node.left = node_left.right
        node_left.right = node
        # 然后几个相关结点的父子关系梳理
        if not node.p:
            root = node_left
            node_left.p = None
        elif node == node.p.left:
            node.p.left = node_left
            node_left.p = node.p
        elif node == node.p.right:
            node.p.right = node_left
            node_left.p = node.p
        node.p = node_left
        # 调整树高， 由node向上层更新树高
        while node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            node = node.p
        return root

    def left_rotate(self, root, node):  # 适用于RR型失衡
        # 还是一样的三个步骤
        node_right = node.right
        node.right = node_right.left
        node_right.left = node
        if not node.p:
            root = node_right
            node_right.p = None
        elif node == node.p.left:
            node.p.left = node_right
            node_right.p = node.p
        elif node == node.p.right:
            node.p.right = node_right
            node_right.p = node.p
        node.p = node_right
        while node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            node = node.p
        return root

    def left_right_rotate(self, root, node):  # LR型失衡
        # 先对左子树左旋, 转为LL型失衡
        root = self.left_rotate(root, node.left)
        root = self.right_rotate(root, node)
        return root

    def right_left_rotate(self, root, node):  # RL型失衡
        # 先对右子树右旋，转为RR型失衡
        root = self.right_rotate(root, node.right)
        root = self.left_rotate(root, node)
        return root

    def balance(self, root, node):
        while node:
            # 调整思路很简单，从node向上层，找到第一个失衡的结点，判断失衡类型，进行相应调整
            if self.get_height(node.left) - self.get_height(node.right) == 2:
                if node.left.left:
                    root = self.right_rotate(root, node)
                else:
                    root = self.left_right_rotate(root, node)
                return root
            elif self.get_height(node.right) - self.get_height(node.left) == 2:
                if node.right.right:
                    root = self.left_rotate(root, node)
                else:
                    root = self.right_left_rotate(root, node)
                return root
            node = node.p
        return root

    def insert(self, root, val):  # 入参:树根及插入值， 返回:新的树根（因为可能会变）
        node = AVLTreeNode(val)
        # 空树 把 root 赋值即可, 无需其他步骤
        if not root:
            return node
        temp = root
        temp_node = None
        # 找到要插入的父节点(temp_node) 若值已存在，则抛出错误
        while temp:
            temp_node = temp
            if node.key < temp.key:
                temp = temp.left
            elif node.key > temp.key:
                temp = temp.right
            else:
                raise KeyError("Error!")
        # 父子相认
        if node.key < temp_node.key:
            temp_node.left = node
        elif node.key > temp_node.key:
            temp_node.right = node
        node.p = temp_node
        # 从父结点 temp_node 开始向上更新每个结点的高度
        temp_p = temp_node
        while temp_p:
            temp_p.height = max(self.get_height(temp_p.left), self.get_height(temp_p.right)) + 1
            temp_p = temp_p.p
        # 最后从插入结点 node本身开始，调整平衡
        root = self.balance(root, node)
        return root


if __name__ == '__main__':
    s = Solution()
    number_list = (7, 4, 1,  # LL
                   8, 5, 12,  # RR
                   9,  # RL
                   3, 2  # RL
                   )
    root = None
    for number in number_list:
        root = s.insert(root, number)
        print(root)


