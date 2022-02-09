# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/7/12. 

class Solution(object):
    '''
    Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.



    Example 1:

    Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    Output: 3
    Explanation: The repeated subarray with maximum length is [3,2,1].
    Example 2:

    Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
    Output: 5


    Constraints:

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 100

    '''
    '''
    ✔️ Solution 1: Dynamic Programming

    It's the same idea with the classic problem Longest Common Subsequence using Dynamic Programming.
    Let dp[i][j] is the longest common suffix between nums1[0..i-1] and nums2[0..j-1].
    
    class Solution:  # 5520 ms, faster than 19.52%
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans
        
    Complexity:
    
    Time: O(M*N), where M <= 1000 is length of nums1, N <= 1000 is length of nums2.
    Space: O(M*N)
    
    ✔️ Solution 2: Dynamic Programming (Space Optimized)
    
    Since our dp only access the previous dp state and current dp state, so we can use 2 variable dp, prevDP which will optimize space to O(N).
    
    class Solution:  # 4724 ms, faster than 34.98%
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2): 
            return self.findLength(nums2, nums1)  # Make sure len(nums1) > len(nums2) to optimize space
        m, n = len(nums1), len(nums2)
        dp, prevDP = [0] * (n+1), [0] * (n+1)
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = prevDP[j-1] + 1
                else:
                    dp[j] = 0
                ans = max(ans, dp[j])
            dp, prevDP = prevDP, dp
        return ans
        
    Complexity:
    
    Time: O(M*N), where M <= 1000 is the maximum, N <= 1000 is the minimum between length of nums1 and length of nums2 coressponding.
    Space: O(N)
    
    ✔️ Solution 3: KMP Solution
    
    Click to see detail
    The basic problem of KMP is that: Given a string s and a pattern p, return the indices of the occurrences of p in s.
    While doing KMP matching between s and p, we can have the longest matching between substring of s with prefix of p.
    The idea is that, we try all patterns p' = p[0..n-1], [1..n-1], ..., [n-1..n-1], and keep update the longest matching between substring of sand patterns p'.
    class Solution:
        def findLength(self, nums1: List[int], nums2: List[int]) -> int:
            if len(nums1) < len(nums2): 
                return self.findLength(nums2, nums1)  # Make sure len(nums1) > len(nums2) to optimize time & space
    
            def computeKMP(pattern):
                n = len(pattern)
                lps = [0] * n
                j = 0
                for i in range(1, n):
                    while j > 0 and pattern[i] != pattern[j]: j = lps[j - 1]
                    if pattern[i] == pattern[j]: j += 1
                    lps[i] = j
                return lps
    
            ans = 0
            while len(nums2) > ans:
                lps = computeKMP(nums2)
                j = 0  # pattern pointer
                for i in range(len(nums1)):
                    while j > 0 and nums1[i] != nums2[j]: j = lps[j - 1]
                    if nums1[i] == nums2[j]: j += 1
                    ans = max(ans, j)  # update longest matching between prefix of P and substring of S so far
                    if j == len(nums2):  # if P was found in S
                        j = lps[j - 1]
                del nums2[0]
            return ans
    Complexity:
    
    Time: O(N*(M + N)), where M <= 1000 is the maximum, N <= 1000 is the minimum between length of nums1 and length of nums2 coressponding.
    Space: O(N)
    
    ✔️ Solution 4: Polynomial rolling hash Solution
    
    Pre-compute Polynomial rolling hash of nums1 and nums2, so that we can get the hash value of an arbitrary subarray in O(1).
    We need to choose a good BASE and MOD so that collision only happens rarely if have.
    BASE should be a prime number >= maximum the maximum of all numbers, here I choose BASE = 101.
    MOD should be a prime number large enough. In C++, I use long long type and leave it overflow by default. In Python, I used a big MOD to limit their value.
    Then we binary search to find the maximum size of subarray which appears in both nums1 and nums2.
    How to check if we can found any subarray of size size in both nums1 and nums2?
    Firstly, we iterate i = 0..m-size+1 to get all hashing values of subarray of size size in the nums1, and put them into HashMap, let name it seen.
    Secondly, we iterate i = 0..n-size+1 to get all hashing values of subarray of size size in the nums2, if any hash is already found in seen, then it's a possible there is a subarray which exists in both nums1 and nums2. To make sure, we can do double-checking for it.
    Return TRUE, if we found a valid subarray which exists in both nums1 and nums2, else return FALSE.
    
    class Solution:  # 156 ms, faster than 98.97%
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        BASE, MOD = 101, 1_000_000_000_001
        hash1, hash2, POW = [0] * (m + 1), [0] * (n + 1), [1] * (max(m, n) + 1)
        for i in range(max(m, n)): POW[i + 1] = POW[i] * BASE % MOD  # Compute POW of BASE
        for i in range(m): hash1[i + 1] = (hash1[i] * BASE + nums1[i]) % MOD  # Compute hashing values of nums1
        for i in range(n): hash2[i + 1] = (hash2[i] * BASE + nums2[i]) % MOD  # Compute hashing values of nums2

        def getHash(h, left, right):  # 0-based indexing, right inclusive
            return (h[right + 1] - h[left] * POW[right - left + 1] % MOD + MOD) % MOD

        def foundSubArray(size):
            seen = defaultdict(list)
            for i in range(m - size + 1):
                h = getHash(hash1, i, i + size - 1)
                seen[h].append(i)
            for i in range(n - size + 1):
                h = getHash(hash2, i, i + size - 1)
                if h in seen:
                    for j in seen[h]:  # Double check - This rarely happens when collision occurs -> No change in time complexity
                        if nums1[j:j + size] == nums2[i:i + size]:
                            return True
            return False

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if foundSubArray(mid):
                ans = mid  # Update answer
                left = mid + 1  # Try to expand size
            else:
                right = mid - 1  # Try to shrink size
        return ans
        
    Complexity:
    
    Time: O((M+N) * logN), where M <= 1000 is the maximum, N <= 1000 is the minimum between length of nums1 and length of nums2 coressponding.
    Space: O(M + N)
    '''
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
