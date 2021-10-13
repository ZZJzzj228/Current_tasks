
# Information Extraction

## Related Efforts
- CCKS2021
- LeetCode

#### CCKS2021
 -  None.

#### LeetCode
Two exercises a week nowadays.

---

- NO.7 整数反转

| # | Title | Solution | Difficulty | Time |
|---| ----- | -------- | ---------- | ---- |
|0007|[reverse-integer](https://leetcode-cn.com/problems/reverse-integer//) | Python3|Easy|30min|

```python
"""
LeetCode NO.7
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
"""

a = input("请输入一个整数")
x = list(str(a))

if x[0] == "-":
    x.remove("-")
    x.reverse()
    r = ''.join(x)
    r = - int(r)

else:
    x.reverse()
    r = ''.join(x)
    r = int(r)

if not -pow(2, 31) <= r <= pow(2, 31) - 1:
    r = 0

print(r)
```
---
- NO.14 最长公共前缀

| # | Title | Solution | Difficulty | Time |
|---| ----- | -------- | ---------- | ---- |
|0014|[longest-common-prefix](https://leetcode-cn.com/problems/longest-common-prefix/) | Python3|Easy|30min|

```python
"""
LeetCode_NO.14_最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
输入：strs = ["flower","flow","flight"]
输出："fl"
"""

strs = ["flower", "flow", "flight", "fl"]
min_len = 300
for i in range(len(strs)):
    if len(strs[i]) < min_len:
        min_len = len(strs[i])      # 找到strs中字符串的最短长度，防止越界

mark = 1        # mark用来记录第j个字符是不是都一样，若一样值为1，为0退出循环
position = 0    # position记录最长公共前缀的最后一位位置（从0开始）
j = 0           # 循环变量
while mark != 0:
    if j == min_len:
        position = j - 1    # 防止越界
        break
    common_char = strs[0][j]
    for i in range(1, len(strs)):
        if strs[i][j] != common_char:
            mark = 0
            position = j - 1
            break
    j += 1
print("最长公共前缀是" + strs[0][:position + 1])
```
---
- NO.21 链表合成

| # | Title | Solution | Difficulty | Time |
|---| ----- | -------- | ---------- | ---- |
|0021|[merge-two-sorted-lists](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | Python3|Easy|5min|

```python
"""
LeetCode_NO.21_链表合成
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""

a = [2, 3, 4]
b = [1, 3, 6, 10]
a = a + b
a.sort()
print(a)
```

---
- NO.26 删除有序数组中的重复项

| # | Title | Solution | Difficulty | Time |
|---| ----- | -------- | ---------- | ---- |
|0026|[remove-duplicates-from-sorted-array](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/) | Python3|Easy|10min|

```python
"""
LeetCode.NO.26_删除有序数组中的重复项
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""

a = [0, 0, 1, 1, 2, 3, 4, 4, 5]
for i in range(len(a) - 1, 0, -1):
    if a[i] == a[i - 1]:
        a.pop(i)
print(len(a))
```

---
- NO.27 移除元素

| # | Title | Solution | Difficulty | Time |
|---| ----- | -------- | ---------- | ---- |
|0027|[remove-element](https://leetcode-cn.com/problems/remove-element/) | Python3|Easy|5min|

```python
"""
LeetCode.NO.27_移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""

a = [0, 0, 1, 1, 2, 3, 4, 4, 5]
val = 4
for i in range(len(a) - 1, 0, -1):
    if a[i] == 4:
        a.pop(i)
print(len(a))
```

---
- NO.1929 列表合并

| # | Title | Solution | Difficulty | Time |
|---| ----- | -------- | ---------- | ---- |
|1929|[concatenation-of-array](https://leetcode-cn.com/problems/concatenation-of-array/) | Python3|Easy|30min|

```python
"""
力扣LeetCode NO.1929
给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：
ans[i] == nums[i]
ans[i + n] == nums[i]
具体而言，ans 由两个 nums 数组 串联 形成。
返回数组 ans 。
"""

a = [1, 2, 3, 4]
b = a + a
print(b)
```

---
## Comments
- Any questions: 273419137@qq.com or 18612535066
Thank you!


