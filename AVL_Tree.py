
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        head = None
        if not nums:
            return head

        def helper(lt, rt):
            if lt == rt:
                return TreeNode(nums[lt])
            mid = (lt + rt) // 2
            p = TreeNode(nums[mid])
            if mid > lt:
                p.left = helper(lt, mid - 1)
            if mid < rt:
                p.right = helper(mid + 1, rt)
            return p

        head = helper(0, len(nums) - 1)
        return head


if __name__ == '__main__':
    arr = [0, 1, 3, 5, 6, 7]
    s = Solution()
    h = s.sortedArrayToBST(arr)
    print(h.val)