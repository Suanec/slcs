"""
- filename: the_leftmost_num_idx.py
- description: 
- author: suanec <shenenzhao@kuaishou.com>
- date: 2025-09-22
"""

"""
问题描述
给定一个 升序排列 的整数数组 nums 和一个目标值 num，找到 num 在数组中 第一次出现的位置（最左索引）。如果 num 不存在，返回 -1。

示例 1：

输入: nums = [1, 2, 2, 2, 3], num = 2
输出: 1
解释: 数字 2 第一次出现在索引 1 处。

示例 2：

输入: nums = [1, 2, 3, 4], num = 5
输出: -1
解释: 5 不在数组中。
"""
class Solution:
  def the_leftmost_num_idx(self, nums, num):
    return self.the_leftmost_num_idx_recursive(nums, num)
    # return self.the_leftmost_num_idx_iteration(nums, num)

  def the_leftmost_num_idx_recursive(self, nums, num):
      left, right = 0, len(nums) - 1
      first_index = -1  # 初始化未找到

      while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == num:
          first_index = mid  # 记录当前找到的位置
          tmp = self.the_leftmost_num_idx_recursive(nums[:mid], num)
          if (tmp > 0 and tmp < first_index):
            return tmp
          else:
            return first_index
        elif nums[mid] < num:
          left = mid + 1
        else:
          right = mid - 1
      return first_index

  def the_leftmost_num_idx_iteration(self, nums, num):
    left, right = 0, len(nums) - 1
    first_index = -1  # 初始化未找到

    while left <= right:
      mid = left + (right - left) // 2
      if nums[mid] == num:
        first_index = mid  # 记录当前找到的位置
        right = mid - 1    # 继续向左搜索
      elif nums[mid] < num:
        left = mid + 1
      else:
        right = mid - 1
    return first_index

if __name__ == '__main__':
  nums = [1, 2, 2, 2, 3]
  print(Solution().the_leftmost_num_idx(nums, 2))
  assert(1 == Solution().the_leftmost_num_idx(nums, 2))  # 输出: 1
  print(Solution().the_leftmost_num_idx(nums, 4))
  assert(-1 == Solution().the_leftmost_num_idx(nums, 4))  # 输出: -1
  nums = [1, 2, 3, 4]
  print(Solution().the_leftmost_num_idx(nums, 2))
  assert(1 == Solution().the_leftmost_num_idx(nums, 2))  # 输出: 1
  print(Solution().the_leftmost_num_idx(nums, 4))
  assert(3 == Solution().the_leftmost_num_idx(nums, 4))  # 输出: 3
  print(Solution().the_leftmost_num_idx(nums, 5))
  assert(-1 == Solution().the_leftmost_num_idx(nums, 5))  # 输出: -1
  nums = [1, 22, 31, 47]
  print(Solution().the_leftmost_num_idx(nums, 31))
  assert(2 == Solution().the_leftmost_num_idx(nums, 31))  # 输出: 2
  print(Solution().the_leftmost_num_idx(nums, 5))
  assert(-1 == Solution().the_leftmost_num_idx(nums, 5))  # 输出: -1
  print("all test passed")

'''
2. LeetCode 275. H-Index II
这道题是进阶版，输入数组 citations 已经按升序排列。要求设计一个 O(log n) 时间的算法。

核心思路：二分查找。
我们需要找到一个点 h，使得：

∙
至少有 n - mid 篇论文的引用次数 >= citations[mid]
∙
并且 citations[mid] >= (n - mid)
步骤：

1.
设 n = len(citations), left = 0, right = n - 1。
2.
while left <= right:
∙
mid = left + (right - left) // 2
∙
papers = n - mid # 引用次数 >= citations[mid] 的论文数量
∙
如果 citations[mid] == papers：找到目标，返回 papers。
∙
如果 citations[mid] < papers：说明 H 指数可能更大，向右找 (left = mid + 1)。
∙
如果 citations[mid] > papers：说明 H 指数可能更小，向左找 (right = mid - 1)。
3.
循环结束后，n - left 就是 H 指数。

class Solution:
  def hIndex(self, citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n - 1

    while left <= right:
      mid = left + (right - left) // 2
      papers = n - mid # 从mid到末尾的论文数量（这些论文的引用次数>=citations[mid]）
      if citations[mid] == papers:
        return papers
      elif citations[mid] < papers:
        # 引用次数太小，需要让引用次数变大（向右移动）
        left = mid + 1
      else:
        # 引用次数太大，需要让引用次数变小（向左移动）
        right = mid - 1
    # 退出循环时，left指向第一个满足citations[i] >= n - i的位置
    return n - left
---

### **总结**
| 题目 | 条件 | 推荐方法 | 时间复杂度 | 空间复杂度 |
| :--- | :--- | :--- | :--- | :--- |
| **274** | 数组未排序 | **计数排序** | `O(n)` | `O(n)` |
|  |  | 排序 | `O(n log n)` | `O(1)` |
| **275** | 数组已升序排序 | **二分查找** | `O(log n)` | `O(1)` |

**最常考且需要掌握的是方法二的计数排序解法。**
'''
