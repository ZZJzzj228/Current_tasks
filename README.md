
# Information Extraction

## Related Efforts
- CCKS2021
- LeetCode

#### CCKS2021
 -  None.

#### LeetCode
Two exercises a week nowadays.
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


