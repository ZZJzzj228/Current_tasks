"""
力扣LeetCode NO.1929
给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：

ans[i] == nums[i]
ans[i + n] == nums[i]
具体而言，ans 由两个 nums 数组 串联 形成。

返回数组 ans 。
"""

a = [1, 2, 3, 4]
b = a + a
print(b)

"""
以下方法将两个列表作为新列表的元素，不符合题意。
import numpy as np

a = [1, 2, 3, 4]
print(np.vstack((a, a)))
"""