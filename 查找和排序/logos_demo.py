import math


def order_find(nums: list, find_x: float) -> bool:
    """

    :param nums: 参数集合
    :param find_x: 目标参数
    :return: 命中结果
    """
    for x in nums:
        if x == find_x:
            return True
    return False


def half_find(nums: list, find_x: float) -> bool:  # 自己实现有待商榷：待编写实际测试函数
    """

    :param nums: 顺序列表
    :param find_x: 目标值
    :return
    """
    half = math.floor(len(nums) / 2)
    print(half)
    print(nums)
    if find_x == nums[half]:
        return True
    elif half == 0:
        return False
    elif find_x > nums[half]:
        return half_find(nums[half + 1:], find_x)

    elif find_x < nums[half]:
        return half_find(nums[0:half], find_x)


def half_find_while(nums: list, find_x: float) -> bool:
    start = 0
    end = len(nums) - 1  # 根据查询区间的不同,while 的条件值不同
    while start <= end:
        mid = math.floor((start + end) / 2)
        print(f"{start},{end},{mid}")
        if nums[mid] == find_x:
            return True
        elif nums[mid] < find_x:
            start = mid + 1
        elif nums[mid] > find_x:
            end = mid - 1
    return False


def hash_find():  # dict 就是哈希表
    pass


def bubble_sort(nums: list):  # 冒泡排序
    for i in range(0, len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:  # 有大则换到后边去
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)


def short_bubble_sort(nums):  # 短冒泡排序 无交换则停止
    for i in range(0, len(nums) - 1):
        Flag = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:  # 有大则换到后边去
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                Flag = True
        print(nums)
        if not Flag:
            break


def choose_sort(nums):  # 选择排序 (减少了了数字交换的频率)
    for i in range(len(nums) - 1):
        k = 0
        for j in range(1, len(nums) - i):
            if nums[k] < nums[j]:
                k = j
        nums[k], nums[j] = nums[j], nums[k]
        print(f"{k},{i}")
        print(nums)


def insert_sort(nums: list):  # 插入排序
    for i in range(1, len(nums)):
        current = nums[i]
        j = i
        while j > 0 and current < nums[j - 1]:
            nums[j] = nums[j - 1]
            j = j - 1
        nums[j] = current
        print(nums)


# nums = [4, 7, 12, 20, 36, 48, 50, 77, 90, 100]


def fast_sort(nums: list):  # 快速排序的时间复杂度
    if len(nums) <= 1:
        return nums
    else:
        mid = nums[0]
        left = []
        right = []
        for i in nums[1:]:
            if i > mid:
                right.append(i)
            else:
                left.append(i)
        print(f"left:{left},mid::{mid},right:{right}")
        return fast_sort(left) + [mid] + fast_sort(right)


# 希尔排序


# 归并排序
def merge_sort(nums: list):
    print(f"split:{nums}")
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i = i + 1
            else:
                nums[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            nums[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            nums[k] = right[j]
            j = j + 1
            k = k + 1
    print("Merging ", nums)


# 二叉树排序
# 堆排序
# 基数排序


nums = [4, 77, 2, 20, 90, 36, 12, 7, 50, 48]
merge_sort(nums)
