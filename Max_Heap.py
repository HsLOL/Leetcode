# coding=utf-8

import numpy as np


class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):  # 时间复杂度 O(n)
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)  # 进行排序前，先将数组转换成大根堆的形式
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]  # 每次将堆顶的元素沉到最下面之后，在将剩余元素构成大根堆
            self.max_heapify(nums, 0, i)

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     self.heap_sort(nums)
    #     return nums

    def sortArray(self, arr):
        self.heap_sort(arr)
        return arr

# class Solution ------------------------------------------------------------------------------------


# test Max Heapify
arr = np.array([10, 6, 7, 5, 15, 17, 12])
tool = Solution()
sort_arr = tool.sortArray(arr)
print(sort_arr)


# list = [10, 6, 7, 5, 15, 17, 12]
# for index in range(len(list) - 1, -1, -1):
#     print(f'index:{index}')
