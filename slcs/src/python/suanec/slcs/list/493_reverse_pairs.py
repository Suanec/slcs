# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2022/1/6.
'''
```
General principles behind problems similar to "Reverse Pairs"
1.3K
fun4LeetCode's avatar
fun4LeetCode
19904
Last Edit: October 26, 2018 3:00 PM

61.8K VIEWS

It looks like a host of solutions are out there (BST-based, BIT-based, Merge-sort-based). Here I'd like to focus on the general principles behind these solutions and its possible application to a number of similar problems.

The fundamental idea is very simple: break down the array and solve for the subproblems.

A breakdown of an array naturally reminds us of subarrays. To smoothen our following discussion, let's assume the input array is nums, with a total of n elements. Let nums[i, j] denote the subarray starting from index i to index j (both inclusive), T(i, j) as the same problem applied to this subarray (for example, for Reverse Pairs, T(i, j) will represent the total number of important reverse pairs for subarray nums[i, j]).

With the definition above, it's straightforward to identify our original problem as T(0, n - 1). Now the key point is how to construct solutions to the original problem from its subproblems. This is essentially equivalent to building recurrence relations for T(i, j). Since if we can find solutions to T(i, j) from its subproblems, we surely can build solutions to larger subarrays until eventually the whole array is spanned.

While there may be many ways for establishing recurrence relations for T(i, j), here I will only introduce the following two common ones:

T(i, j) = T(i, j - 1) + C, i.e., elements will be processed sequentially and C denotes the subproblem for processing the last element of subarray nums[i, j]. We will call this sequential recurrence relation.

T(i, j) = T(i, m) + T(m + 1, j) + C where m = (i+j)/2, i.e., subarray nums[i, j] will be further partitioned into two parts and C denotes the subproblem for combining the two parts. We will call this partition recurrence relation.

For either case, the nature of the subproblem C will depend on the problem under consideration, and it will determine the overall time complexity of the original problem. So usually it's crucial to find efficient algorithm for solving this subproblem in order to have better time performance. Also pay attention to possibilities of overlapping subproblems, in which case a dynamic programming (DP) approach would be preferred.

Next, I will apply these two recurrence relations to this problem "Reverse Pairs" and list some solutions for your reference.

I -- Sequential recurrence relation

Again we assume the input array is nums with n elements and T(i, j) denotes the total number of important reverse pairs for subarray nums[i, j]. For sequential recurrence relation, we can set i = 0, i.e., the subarray always starts from the beginning. Therefore we end up with:

T(0, j) = T(0, j - 1) + C

where the subproblem C now becomes "find the number of important reverse pairs with the first element of the pair coming from subarray nums[0, j - 1] while the second element of the pair being nums[j]".

Note that for a pair (p, q) to be an important reverse pair, it has to satisfy the following two conditions:

p < q: the first element must come before the second element;
nums[p] > 2 * nums[q]: the first element has to be greater than twice of the second element.
For subproblem C, the first condition is met automatically; so we only need to consider the second condition, which is equivalent to searching for all elements within subarray nums[0, j - 1] that are greater than twice of nums[j].

The straightforward way of searching would be a linear scan of the subarray, which runs at the order of O(j). From the sequential recurrence relation, this leads to the naive O(n^2) solution.

To improve the searching efficiency, a key observation is that the order of elements in the subarray does not matter, since we are only interested in the total number of important reverse pairs. This suggests we may sort those elements and do a binary search instead of a plain linear scan.

If the searching space (formed by elements over which the search will be done) is "static" (it does not vary from run to run), placing the elements into an array would be perfect for us to do the binary search. However, this is not the case here. After the j-th element is processed, we need to add it to the searching space so that it becomes searchable for later elements, which renders the searching space expanding as more and more elements are processed.

Therefore we'd like to strike a balance between searching and insertion operations. This is where data structures like binary search tree (BST) or binary indexed tree (BIT) prevail, which offers relatively fast performance for both operations.

1. BST-based solution

we will define the tree node as follows, where val is the node value and cnt is the total number of elements in the subtree rooted at current node that are greater than or equal to val:

class Node {
    int val, cnt;
    Node left, right;
        
    Node(int val) {
        this.val = val;
        this.cnt = 1;
    }
}
The searching and insertion operations can be done as follows:

private int search(Node root, long val) {
    if (root == null) {
    	return 0;
    } else if (val == root.val) {
    	return root.cnt;
    } else if (val < root.val) {
    	return root.cnt + search(root.left, val);
    } else {
    	return search(root.right, val);
    }
}

private Node insert(Node root, int val) {
    if (root == null) {
        root = new Node(val);
    } else if (val == root.val) {
        root.cnt++;
    } else if (val < root.val) {
        root.left = insert(root.left, val);
    } else {
        root.cnt++;
        root.right = insert(root.right, val);
    }
    
    return root;
}
And finally the main program, in which we will search for all elements no less than twice of current element plus 1 (converted to long type to avoid overflow) while insert the element itself into the BST.

Note: this homemade BST is not self-balanced and the time complexity can go as bad as O(n^2) (in fact you will get TLE if you copy and paste the solution here). To guarantee O(nlogn) performance, use one of the self-balanced BST's (e.g. Red-black tree, AVL tree, etc.).

public int reversePairs(int[] nums) {
    int res = 0;
    Node root = null;
    	
    for (int ele : nums) {
        res += search(root, 2L * ele + 1);
        root = insert(root, ele);
    }
    
    return res;
}
2. BIT-based solution

For BIT, the searching and insertion operations are:

private int search(int[] bit, int i) {
    int sum = 0;
    
    while (i < bit.length) {
        sum += bit[i];
        i += i & -i;
    }

    return sum;
}

private void insert(int[] bit, int i) {
    while (i > 0) {
        bit[i] += 1;
        i -= i & -i;
    }
}
And the main program, where again we will search for all elements greater than twice of current element while insert the element itself into the BIT. For each element, the "index" function will return its index in the BIT. Unlike the BST-based solution, this is guaranteed to run at O(nlogn).

public int reversePairs(int[] nums) {
    int res = 0;
    int[] copy = Arrays.copyOf(nums, nums.length);
    int[] bit = new int[copy.length + 1];
    
    Arrays.sort(copy);
    
    for (int ele : nums) {
        res += search(bit, index(copy, 2L * ele + 1));
        insert(bit, index(copy, ele));
    }
    
    return res;
}

private int index(int[] arr, long val) {
    int l = 0, r = arr.length - 1, m = 0;
    	
    while (l <= r) {
    	m = l + ((r - l) >> 1);
    		
    	if (arr[m] >= val) {
    	    r = m - 1;
    	} else {
    	    l = m + 1;
    	}
    }
    
    return l + 1;
}
More explanation for the BIT-based solution:

We want the elements to be sorted so there is a sorted version of the input array which is copy.

The bit is built upon this sorted array. Its length is one greater than that of the copy array to account for the root.

Initially the bit is empty and we start doing a sequential scan of the input array. For each element being scanned, we first search the bit to find all elements greater than twice of it and add the result to res. We then insert the element itself into the bit for future search.

Note that conventionally searching of the bit involves traversing towards the root from some index of the bit, which will yield a predefined running total of the copy array up to the corresponding index. For insertion, the traversing direction will be opposite and go from some index towards the end of the bit array.

For each scanned element of the input array, its searching index will be given by the index of the first element in the copy array that is greater than twice of it (shifted up by 1 to account for the root), while its insertion index will be the index of the first element in the copy array that is no less than itself (again shifted up by 1). This is what the index function is for.

For our case, the running total is simply the number of elements encountered during the traversal process. If we stick to the convention above, the running total will be the number of elements smaller than the one at the given index, since the copy array is sorted in ascending order. However, we'd actually like to find the number of elements greater than some value (i.e., twice of the element being scanned), therefore we need to flip the convention. This is what you see inside the search and insert functions: the former traversing towards the end of the bit while the latter towards the root.

II -- Partition recurrence relation

For partition recurrence relation, setting i = 0, j = n - 1, m = (n-1)/2, we have:

T(0, n - 1) = T(0, m) + T(m + 1, n - 1) + C

where the subproblem C now reads "find the number of important reverse pairs with the first element of the pair coming from the left subarray nums[0, m] while the second element of the pair coming from the right subarray nums[m + 1, n - 1]".

Again for this subproblem, the first of the two aforementioned conditions is met automatically. As for the second condition, we have as usual this plain linear scan algorithm, applied for each element in the left (or right) subarray. This, to no surprise, leads to the O(n^2) naive solution.

Fortunately the observation holds true here that the order of elements in the left or right subarray does not matter, which prompts sorting of elements in both subarrays. With both subarrays sorted, the number of important reverse pairs can be found in linear time by employing the so-called two-pointer technique: one pointing to elements in the left subarray while the other to those in the right subarray and both pointers will go only in one direction due to the ordering of the elements.

The last question is which algorithm is best here to sort the subarrays. Since we need to partition the array into halves anyway, it is most natural to adapt it into a Merge-sort. Another point in favor of Merge-sort is that the searching process above can be embedded seamlessly into its merging stage.

So here is the Merge-sort-based solution, where the function "reversePairsSub" will return the total number of important reverse pairs within subarray nums[l, r]. The two-pointer searching process is represented by the nested while loop involving variable p, while the rest is the standard merging algorithm.

public int reversePairs(int[] nums) {
    return reversePairsSub(nums, 0, nums.length - 1);
}
    
private int reversePairsSub(int[] nums, int l, int r) {
    if (l >= r) return 0;
        
    int m = l + ((r - l) >> 1);
    int res = reversePairsSub(nums, l, m) + reversePairsSub(nums, m + 1, r);
        
    int i = l, j = m + 1, k = 0, p = m + 1;
    int[] merge = new int[r - l + 1];
        
    while (i <= m) {
        while (p <= r && nums[i] > 2 L * nums[p]) p++;
        res += p - (m + 1);
				
        while (j <= r && nums[i] >= nums[j]) merge[k++] = nums[j++];
        merge[k++] = nums[i++];
    }
        
    while (j <= r) merge[k++] = nums[j++];
        
    System.arraycopy(merge, 0, nums, l, merge.length);
        
    return res;
}
III -- Summary

Many problems involving arrays can be solved by breaking down the problem into subproblems applied on subarrays and then link the solution to the original problem with those of the subproblems, to which we have sequential recurrence relation and partition recurrence relation. For either case, it's crucial to identify the subproblem C and find efficient algorithm for approaching it.

If the subproblem C involves searching on "dynamic searching space", try to consider data structures that support relatively fast operations on both searching and updating (such as self-balanced BST, BIT, Segment tree, ...).

If the subproblem C of partition recurrence relation involves sorting, Merge-sort would be a nice sorting algorithm to use. Also, the code could be made more elegant if the solution to the subproblem can be embedded into the merging process.

If there are overlapping among the subproblems T(i, j), it's preferable to cache the intermediate results for future lookup.

Lastly let me name a few leetcode problems that fall into the patterns described above and thus can be solved with similar ideas.

315. Count of Smaller Numbers After Self
327. Count of Range Sum

For leetcode 315, applying the sequential recurrence relation (with j fixed), the subproblem C reads: find the number of elements out of visited ones that are smaller than current element, which involves searching on "dynamic searching space"; applying the partition recurrence relation, we have a subproblem C: for each element in the left half, find the number of elements in the right half that are smaller than it, which can be embedded into the merging process by noting that these elements are exactly those swapped to its left during the merging process.

For leetcode 327, applying the sequential recurrence relation (with j fixed) on the pre-sum array, the subproblem C reads: find the number of elements out of visited ones that are within the given range, which again involves searching on "dynamic searching space"; applying the partition recurrence relation, we have a subproblem C: for each element in the left half, find the number of elements in the right half that are within the given range, which can be embedded into the merging process using the two-pointer technique.

Anyway, hope these ideas can sharpen your skills for solving array-related problems.
```

---
```
看起来有很多解决方案（基于 BST、基于 BIT、基于合并排序）。在这里，我想重点介绍这些解决方案背后的一般原则及其在许多类似问题上的可能应用。

基本思想非常简单：分解数组并解决子问题。

数组的分解自然会让我们想起子数组。为了使我们接下来的讨论更顺畅，让我们假设输入数组是 nums，总共有 n 个元素。让 nums[i, j] 表示从索引 i 开始到索引 j（两者都包括在内）的子数组，T(i, j) 与应用于此子数组的问题相同（例如，对于 Reverse Pairs，T(i, j)将表示子数组 nums[i, j]) 的重要反向对的总数。

根据上面的定义，很容易将我们的原始问题识别为 T(0, n - 1)。现在的关键是如何从原始问题的子问题构建解决方案。这本质上等同于为 T(i, j) 建立递推关系。因为如果我们可以从 T(i, j) 的子问题中找到它的解，我们肯定可以构建更大的子数组的解，直到最终整个数组被跨越。

虽然建立T(i,j)递推关系的方法可能有很多种，这里我只介绍以下两种常见的：

T(i, j) = T(i, j - 1) + C，即依次处理元素，C表示处理子数组nums[i,j]最后一个元素的子问题。我们称这种顺序递推关系。

T(i, j) = T(i, m) + T(m + 1, j) + C 其中 m = (i+j)/2，即子数组 nums[i, j] 将被进一步划分为两个部分和 C 表示组合两个部分的子问题。我们将称之为分区递推关系。

对于任何一种情况，子问题 C 的性质将取决于所考虑的问题，它将决定原始问题的整体时间复杂度。因此，为了获得更好的时间性能，找到解决这个子问题的有效算法通常是至关重要的。还要注意重叠子问题的可能性，在这种情况下，动态规划 (DP) 方法将是首选。

接下来，我将把这两个递推关系应用到这个问题“Reverse Pairs”，并列出一些解决方案供您参考。

I -- 顺序递推关系

我们再次假设输入数组是具有 n 个元素的 nums 并且 T(i, j) 表示子数组 nums[i, j] 的重要反向对的总数。对于顺序递推关系，我们可以设置 i = 0，即子数组总是从头开始。因此我们最终得到：
T(0, j) = T(0, j - 1) + C

where the subproblem C now becomes "find the number of important reverse pairs with the first element of the pair coming from subarray nums[0, j - 1] while the second element of the pair being nums[j]".

这里子问题C化简为：当逆序对的组成是：第一个元素来自于nums[0, j - 1]，第二个元素是nums[j]。寻找逆序对的数量。


请注意，要使一对 (p, q) 成为重要的逆序对，它必须满足以下两个条件：

p < q：第一个元素必须在第二个元素之前；
nums[p] > 2 * nums[q]：第一个元素必须大于第二个元素的两倍。
对于子问题C，第一个条件自动满足；所以我们只需要考虑第二个条件，相当于在子数组nums[0, j - 1]中搜索所有大于nums[j]两倍的元素。

The straight forward way of searching would be a linear scan of the subarray, which runs at the order of O(j). From the sequential recurrence relation, this leads to the naive O(n^2) solution.
最直接的方法就是线性扫描第一部分的子序列，时间复杂度O(J)，整体来看，解决方案的复杂度为 朴素的 O(n^2) 。

为了提高搜索效率，一个关键的观察是子数组中元素的顺序无关紧要，因为我们只对重要反向对的总数感兴趣。这表明我们可以对这些元素进行排序并进行二分搜索而不是简单的线性扫描。

如果搜索空间（由将在其上进行搜索的元素形成）是“静态的”（它不会因运行而异），则将元素放入数组将非常适合我们进行二分搜索。 但是，这里的情况并非如此。 在处理完第 j 个元素后，我们需要将其添加到搜索空间中，以便它可以被后面的元素搜索到，这使得搜索空间随着越来越多的元素被处理而扩大。

Therefore we'd like to strike a balance between searching and insertion operations. This is where data structures like binary search tree (BST) or binary indexed tree (BIT) prevail, which offers relatively fast performance for both operations.
因此，我们希望在搜索和插入操作之间做一个折中。 这是二叉搜索树 (BST) 或二叉索引树 (BIT) 等数据结构盛行的地方，它为这两种操作提供了相对较快的性能。

1.基于BST的解决方案
我们将如下定义树节点，其中 val 是节点值，cnt 是以当前节点为根的子树中大于或等于 val 的元素总数：
1. BST-based solution

we will define the tree node as follows, where val is the node value and cnt is the total number of elements in the subtree rooted at current node that are greater than or equal to val:

class Node {
    int val, cnt;
    Node left, right;
        
    Node(int val) {
        this.val = val;
        this.cnt = 1;
    }
}
The searching and insertion operations can be done as follows:

private int search(Node root, long val) {
    if (root == null) {
    	return 0;
    } else if (val == root.val) {
    	return root.cnt;
    } else if (val < root.val) {
    	return root.cnt + search(root.left, val);
    } else {
    	return search(root.right, val);
    }
}

private Node insert(Node root, int val) {
    if (root == null) {
        root = new Node(val);
    } else if (val == root.val) {
        root.cnt++;
    } else if (val < root.val) {
        root.left = insert(root.left, val);
    } else {
        root.cnt++;
        root.right = insert(root.right, val);
    }
    
    return root;
}

最后是主程序，在将元素本身插入到BST中的同时，我们将搜索不少于当前元素加1（转换为long类型以避免溢出）的两倍的所有元素。

注意：这个自制的 BST 不是自平衡的，时间复杂度可能像 O(n^2) 一样糟糕（事实上，如果你在这里复制和粘贴解决方案，你会得到 TLE）。为了保证 O(nlogn) 性能，请使用自平衡 BST 之一（例如红黑树、AVL 树等）。

And finally the main program, in which we will search for all elements no less than twice of current element plus 1 (converted to long type to avoid overflow) while insert the element itself into the BST.

Note: this homemade BST is not self-balanced and the time complexity can go as bad as O(n^2) (in fact you will get TLE if you copy and paste the solution here). To guarantee O(nlogn) performance, use one of the self-balanced BST's (e.g. Red-black tree, AVL tree, etc.).

public int reversePairs(int[] nums) {
    int res = 0;
    Node root = null;
    	
    for (int ele : nums) {
        res += search(root, 2L * ele + 1);
        root = insert(root, ele);
    }
    
    return res;
}


2. BIT-based solution

For BIT, the searching and insertion operations are:

private int search(int[] bit, int i) {
    int sum = 0;
    
    while (i < bit.length) {
        sum += bit[i];
        i += i & -i;
    }

    return sum;
}

private void insert(int[] bit, int i) {
    while (i > 0) {
        bit[i] += 1;
        i -= i & -i;
    }
}
And the main program, where again we will search for all elements greater than twice of current element while insert the element itself into the BIT. For each element, the "index" function will return its index in the BIT. Unlike the BST-based solution, this is guaranteed to run at O(nlogn).

public int reversePairs(int[] nums) {
    int res = 0;
    int[] copy = Arrays.copyOf(nums, nums.length);
    int[] bit = new int[copy.length + 1];
    
    Arrays.sort(copy);
    
    for (int ele : nums) {
        res += search(bit, index(copy, 2L * ele + 1));
        insert(bit, index(copy, ele));
    }
    
    return res;
}

private int index(int[] arr, long val) {
    int l = 0, r = arr.length - 1, m = 0;
    	
    while (l <= r) {
    	m = l + ((r - l) >> 1);
    		
    	if (arr[m] >= val) {
    	    r = m - 1;
    	} else {
    	    l = m + 1;
    	}
    }
    
    return l + 1;
}
More explanation for the BIT-based solution:

We want the elements to be sorted so there is a sorted version of the input array which is copy.

The bit is built upon this sorted array. Its length is one greater than that of the copy array to account for the root.

Initially the bit is empty and we start doing a sequential scan of the input array. For each element being scanned, we first search the bit to find all elements greater than twice of it and add the result to res. We then insert the element itself into the bit for future search.

Note that conventionally searching of the bit involves traversing towards the root from some index of the bit, which will yield a predefined running total of the copy array up to the corresponding index. For insertion, the traversing direction will be opposite and go from some index towards the end of the bit array.

For each scanned element of the input array, its searching index will be given by the index of the first element in the copy array that is greater than twice of it (shifted up by 1 to account for the root), while its insertion index will be the index of the first element in the copy array that is no less than itself (again shifted up by 1). This is what the index function is for.
对于输入数组的每个扫描元素，其搜索索引将由复制数组中第一个元素的索引给出，该索引大于其两倍（向上移动 1 以考虑根），而其插入索引将是复制数组中不小于自身的第一个元素的索引（再次向上移动 1）。这就是索引函数的用途。

For our case, the running total is simply the number of elements encountered during the traversal process. If we stick to the convention above, the running total will be the number of elements smaller than the one at the given index, since the copy array is sorted in ascending order. However, we'd actually like to find the number of elements greater than some value (i.e., twice of the element being scanned), therefore we need to flip the convention. This is what you see inside the search and insert functions: the former traversing towards the end of the bit while the latter towards the root.
对于我们的例子，运行总数只是在遍历过程中遇到的元素数。如果我们坚持上面的约定，运行总数将是小于给定索引处的元素数，因为复制数组是按升序排序的。然而，我们实际上想要找到大于某个值的元素数量（即被扫描元素的两倍），因此我们需要翻转约定。这就是您在搜索和插入函数中看到的：前者遍历到位的末尾，而后者遍历到根。


II -- Partition recurrence relation

For partition recurrence relation, setting i = 0, j = n - 1, m = (n-1)/2, we have:

T(0, n - 1) = T(0, m) + T(m + 1, n - 1) + C

where the subproblem C now reads "find the number of important reverse pairs with the first element of the pair coming from the left subarray nums[0, m] while the second element of the pair coming from the right subarray nums[m + 1, n - 1]".

Again for this subproblem, the first of the two aforementioned（前述的） conditions is met automatically. As for the second condition, we have as usual this plain linear scan algorithm, applied for each element in the left (or right) subarray. This, to no surprise, leads to the O(n^2) naive solution.

Fortunately the observation holds true here that the order of elements in the left or right subarray does not matter, which prompts（提示） sorting of elements in both subarrays. With both subarrays sorted, the number of important reverse pairs can be found in linear time by employing the so-called two-pointer technique: one pointing to elements in the left subarray while the other to those in the right subarray and both pointers will go only in one direction due to the ordering of the elements.

The last question is which algorithm is best here to sort the subarrays. Since we need to partition the array into halves anyway, it is most natural to adapt it into a Merge-sort. Another point in favor of Merge-sort is that the searching process above can be embedded seamlessly into its merging stage.

So here is the Merge-sort-based solution, where the function "reversePairsSub" will return the total number of important reverse pairs within subarray nums[l, r]. The two-pointer searching process is represented by the nested while loop involving variable p, while the rest is the standard merging algorithm.

public int reversePairs(int[] nums) {
    return reversePairsSub(nums, 0, nums.length - 1);
}
    
private int reversePairsSub(int[] nums, int l, int r) {
    if (l >= r) return 0;
        
    int m = l + ((r - l) >> 1);
    int res = reversePairsSub(nums, l, m) + reversePairsSub(nums, m + 1, r);
        
    int i = l, j = m + 1, k = 0, p = m + 1;
    int[] merge = new int[r - l + 1];
        
    while (i <= m) {
        while (p <= r && nums[i] > 2 L * nums[p]) p++;
        res += p - (m + 1);
				
        while (j <= r && nums[i] >= nums[j]) merge[k++] = nums[j++];
        merge[k++] = nums[i++];
    }
        
    while (j <= r) merge[k++] = nums[j++];
        
    System.arraycopy(merge, 0, nums, l, merge.length);
        
    return res;
}

III -- 总结

许多涉及数组的问题可以通过将问题分解为应用于子数组的子问题，然后将原始问题的解决方案与子问题的解决方案联系起来来解决，我们有顺序递推关系和分区递推关系。对于任何一种情况，识别子问题 C 并找到解决它的有效算法都是至关重要的。

如果子问题 C 涉及在“动态搜索空间”上搜索，请尝试考虑在搜索和更新上都支持相对快速操作的数据结构（例如自平衡 BST、BIT、Segment 树……）。

如果分区递推关系的子问题 C 涉及排序，则合并排序将是一个很好的排序算法。此外，如果可以将子问题的解决方案嵌入到合并过程中，则可以使代码更加优雅。

如果子问题 T(i, j) 之间存在重叠，则最好缓存中间结果以供将来查找。

最后让我列举一些属于上述模式的 leetcode 问题，因此可以用类似的想法解决。

315. Count of Smaller Numbers After Self
327. Count of Range Sum

对于leetcode 315，应用顺序递推关系（j固定），子问题C为：从访问过的元素中找出小于当前元素的元素个数，这涉及在“动态搜索空间”上进行搜索；应用分区递推关系，我们有一个子问题C：对于左半部分的每个元素，找到右半部分小于它的元素的数量，可以通过注意到这些元素恰好是合并过程来嵌入到合并过程中那些在合并过程中交换到左边的。

对于leetcode 327，在pre-sum数组上应用顺序递推关系（j固定），子问题C读取：在给定范围内的访问过的元素中找到元素的数量，这再次涉及搜索“动态搜索空间”;应用分区递推关系，我们有一个子问题C：对于左半部分的每个元素，找到给定范围内的右半部分元素的数量，可以使用双指针技术将其嵌入到合并过程中.

无论如何，希望这些想法可以提高您解决阵列相关问题的技能。


```'''
class Solution(object):
    '''
    493. Reverse Pairs
    Hard

    2292

    168

    Add to List

    Share
    Given an integer array nums, return the number of reverse pairs in the array.

    A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].



    Example 1:

    Input: nums = [1,3,2,3,1]
    Output: 2 [3,1] [3,1]

    Example 2:

    Input: nums = [2,4,3,5,1]
    Output: 3


    Constraints:

    1 <= nums.length <= 5 * 10^4
    -231 <= nums[i] <= 2^31 - 1
    Accepted
    72,441
    Submissions
    247,671
    '''
    def value_index_inverted_index(self, _nums):
        inverted_index = {}
        for (idx, value) in enumerate(_nums):
            value_index_list = inverted_index.get(value, [])
            value_index_list.append(idx)
            inverted_index[value] = value_index_list
        inverted_index_keys = sorted(inverted_index.keys())
        return inverted_index_keys, inverted_index

    def judge_reverse_pairs(self, cur_idx, cur_value, other_idx, other_value):
        '''
        0 <= i < j < nums.length and nums[i] > 2 * nums[j]
        :param cur_idx:
        :param cur_value:
        :param other_idx:
        :param other_value:
        :return:
        '''
        if(cur_idx < other_idx):
            if(cur_value > 2 * other_value):
                return True
        return False

    def reversePairs(self, nums):
        """
        :param nums:
        :return:
        """
        # return self.reversePairs_tranverse_TLE(nums)
        return self.reversePairs_merge_sort(nums)


    def reversePairs_tranverse_TLE(self, nums):
        """
        Time Limit Exceeded
        :type nums: List[int]
        :rtype: int
        """
        reverse_pair_count = 0
        for (cur_idx, cur_value) in enumerate(nums):
            other_base_idx = cur_idx + 1
            for (other_idx, other_value) in enumerate(nums[other_base_idx:]):
                if(self.judge_reverse_pairs(cur_idx, cur_value, other_idx + other_base_idx, other_value)):
                    reverse_pair_count += 1
        return reverse_pair_count

    def reversePairs_merge_sort(self, nums):
        """
        # return self.reversePairsSub(nums, 0, len(nums)-1)
        Runtime: 1758 ms, faster than 75.51% of Python online submissions for Reverse Pairs.
        Memory Usage: 19.6 MB, less than 50.00% of Python online submissions for Reverse Pairs.
        return self.reversePairsSelf(nums, 0, len(nums) -1)
        Runtime: 2100 ms, faster than 65.31% of Python online submissions for Reverse Pairs.
        Memory Usage: 19.9 MB, less than 32.65% of Python online submissions for Reverse Pairs.

        :param nums:
        :return:
        """
        # return self.reversePairsSub(nums, 0, len(nums)-1)
        return self.reversePairsSelf(nums, 0, len(nums) -1)

    def reversePairsSub(self, nums, left, right):
        '''
        private int reversePairsSub(int[] nums, int l, int r) {
            if (l >= r) return 0;

            int m = l + ((r - l) >> 1);
            int res = reversePairsSub(nums, l, m) + reversePairsSub(nums, m + 1, r);

            int i = l, j = m + 1, k = 0, p = m + 1;
            int[] merge = new int[r - l + 1];

            while (i <= m) {
                while (p <= r && nums[i] > 2 L * nums[p]) p++;
                res += p - (m + 1);

                while (j <= r && nums[i] >= nums[j]) merge[k++] = nums[j++];
                merge[k++] = nums[i++];
            }

            while (j <= r) merge[k++] = nums[j++];

            System.arraycopy(merge, 0, nums, l, merge.length);

            return res;
        }
        :param left:
        :param right:
        :return:
        '''
        if(left >= right): return 0

        middle = left + ((right - left) >> 1)
        rst = self.reversePairsSub(nums, left, middle) + self.reversePairsSub(nums, middle + 1, right)

        i,j,k,p = left, middle + 1, 0, middle + 1
        merge = [0] * (right - left + 1)
        while(i <= middle):
            while(p <= right and nums[i] > 2 * nums[p]): p += 1
            rst += p - (middle + 1)

            while(j <= right and nums[i] >= nums[j]) :
                merge[k] = nums[j]
                k += 1
                j += 1
            merge[k] = nums[i]
            k += 1; i += 1
        while(j <= right):
            merge[k] = nums[j]
            k += 1
            j += 1
        nums[left:left + len(merge)] = merge[0:]
        return rst

    def reversePairsSelf(self, nums, left, right):
        if(left >= right): return 0

        middle = left + ((right - left) >> 1)
        # divide input array into two parts
        # and check count of important reverse pairs in each subarray
        # last sort which is merge sort each subarray overwrite the origin input array. asc order
        # result is sum of two count of important reverse pairs in each subarray
        result = self.reversePairsSelf(nums, left, middle) + self.reversePairsSelf(nums, middle + 1, right)

        # then use sorted nums to check important reverse pairs in cur input array nums.
        i = left; j = p = middle + 1; k = 0
        merge = [0] * (right - left + 1)

        while(i <= middle):
            p = middle + 1
            while(p <= right and nums[i] > 2 * nums[p]):
                p += 1
                result += 1
            """
            more efficient:
            while(p <= right and nums[i] > 2 * nums[p]):
                p += 1
            result += p - (middle + 1)
            because left and right two subarray both ordered.
            that ensured nums[i] > nums[i-1], and num[p] > num[p-1]
            so while nums[i] > 2 * num[p], nums[i] > 2 * nums[p] > 2 * nums[p-1]   
            from this we can found: we need not tranverse the part of right subarray before p
            but the result need add (p - p_start) equals to p - (middle + 1), 
            contain the left part of right subarray before p
            """

            while(j <= right and nums[i] > nums[j]):
                merge[k] = nums[j]
                k += 1; j += 1
            merge[k] = nums[i]
            k += 1; i += 1
        while(j <= right):
            merge[k] = nums[j]
            k += 1; j += 1

        nums[left:right + 1] = merge
        return result




    def self_testing(self):
        # print(self.value_index_inverted_index([1,3,2,3,1]))
        # 2
        print(self.reversePairs([1,3,2,3,1]))
        # 3
        print(self.reversePairs([2,4,3,5,1]))
        # 0
        print(self.reversePairs([]))

Solution().self_testing()