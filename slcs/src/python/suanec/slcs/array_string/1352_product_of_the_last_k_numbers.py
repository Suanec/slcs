# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/6. 

class ProductOfNumbers(object):
    """
    1352. Product of the Last K Numbers
    Medium

    544

    29

    Add to List

    Share
    Implement the class ProductOfNumbers that supports two methods:

    1. add(int num)

    Adds the number num to the back of the current list of numbers.
    2. getProduct(int k)

    Returns the product of the last k numbers in the current list.
    You can assume that always the current list has at least k numbers.
    At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.



    Example:

    Input
    ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
    [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

    Output
    [null,null,null,null,null,null,20,40,0,null,32]

    Explanation
    ProductOfNumbers productOfNumbers = new ProductOfNumbers();
    productOfNumbers.add(3);        // [3]
    productOfNumbers.add(0);        // [3,0]
    productOfNumbers.add(2);        // [3,0,2]
    productOfNumbers.add(5);        // [3,0,2,5]
    productOfNumbers.add(4);        // [3,0,2,5,4]
    productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
    productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
    productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
    productOfNumbers.add(8);        // [3,0,2,5,4,8]
    productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32


    Constraints:

    There will be at most 40000 operations considering both add and getProduct.
    0 <= num <= 100
    1 <= k <= 40000
    """

    def __init__(self):
        self.data = []
        self.product = 1

    def add(self, num):
        if num != 0:
            self.product *= num
            self.data.append(self.product)
        else:
            self.data = []
            self.product = 1

    def getProduct(self, k):
        """
        Runtime: 284 ms, faster than 39.33% of Python online submissions for Product of the Last K Numbers.
        Memory Usage: 30.5 MB, less than 18.00% of Python online submissions for Product of the Last K Numbers.

        Runtime: 268 ms, faster than 86.67% of Python online submissions for Product of the Last K Numbers.
        Memory Usage: 30.1 MB, less than 88.00% of Python online submissions for Product of the Last K Numbers.

        Runtime: 252 ms, faster than 99.33% of Python online submissions for Product of the Last K Numbers.
        Memory Usage: 30.5 MB, less than 21.33% of Python online submissions for Product of the Last K Numbers.
        :param k:
        :return:
        """
        if len(self.data) < k:
            return 0
        if len(self.data) == k:
            return self.data[-1]
        else:
            return int(self.data[-1] / self.data[-1-k])

    def __init__self(self):
        self.inner_list = []
        self.indexed_product_memo = []
        # memo_index_start and memo_index_end means memo usable value left close and right open.
        self.memo_index_start = len(self.indexed_product_memo) - 1
        self.memo_index_end = self.memo_index_start + 1
        self.last_zero_index = -1


    def add_self(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.inner_list.append(num)
        if(num == 0):
            self.last_zero_index = len(self.inner_list) -1
            self.indexed_product_memo = [0] * len(self.inner_list)
            self.memo_index_start = 0
            self.memo_index_end = len(self.indexed_product_memo)
        else:
            self.indexed_product_memo.append(num)
            self.memo_index_start = len(self.indexed_product_memo) -1
            self.memo_index_end = len(self.indexed_product_memo)

    def getProduct_self(self, k):
        """
        Runtime: 456 ms, faster than 5.33% of Python online submissions for Product of the Last K Numbers.
        Memory Usage: 30.2 MB, less than 88.00% of Python online submissions for Product of the Last K Numbers.
        :type k: int
        :rtype: int
        """
        rst = 1
        # memo_need_start = len_inner_list - (k -1)
        self.len_inner_list = len(self.inner_list)
        memo_need_start = self.len_inner_list - k
        memo_need_end = self.len_inner_list
        if(memo_need_start <= self.last_zero_index):
            return 0
        if(self.memo_index_end == 0): # first call getProduct and without zero in list
            self.memo_index_start = memo_need_start
            self.memo_index_end = memo_need_end
            for idx in xrange(self.memo_index_end -1, self.memo_index_start -1, -1):
                cur_num = self.inner_list[idx]
                self.indexed_product_memo[idx] = cur_num if(idx == self.memo_index_end -1) else cur_num * self.indexed_product_memo[idx + 1]
            return self.indexed_product_memo[memo_need_start]
        else: # already called getProduct before
            if(self.memo_index_end == memo_need_end): # add no num after last getProduct
                if(memo_need_start >= self.memo_index_start): # cur k less than exist call getProduct k
                    return self.indexed_product_memo[memo_need_start]
                else: # cur k larger than exist call getProduct k
                    for idx in xrange(self.memo_index_start - 1 , memo_need_start -1, -1):
                        cur_num = self.inner_list[idx]
                        self.indexed_product_memo[idx] = cur_num if(idx == self.memo_index_end -1) else cur_num * self.indexed_product_memo[idx + 1]
                    self.memo_index_start = memo_need_start
                    self.memo_index_end = memo_need_end
                    return self.indexed_product_memo[memo_need_start]
            else: # add num after exist call getProduct

                self.memo_index_start = memo_need_start
                self.memo_index_end = memo_need_end
                for idx in xrange(self.memo_index_end -1, self.memo_index_start -1, -1):
                    cur_num = self.inner_list[idx]
                    self.indexed_product_memo[idx] = cur_num if(idx == self.memo_index_end -1) else cur_num * self.indexed_product_memo[idx + 1]
                return self.indexed_product_memo[memo_need_start]

    """
    Time Limit Exceeded
    """
    def add_tle(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.inner_list.append(num)

    def getProduct_tle(self, k):
        """
        :type k: int
        :rtype: int
        """
        rst = 1
        start_idx = len(self.inner_list) -1
        for idx in xrange(0, k):
            rst *= self.inner_list[start_idx - idx]
        return rst


        # Your ProductOfNumbers object will be instantiated and called as such:
        # obj = ProductOfNumbers()
        # obj.add(num)
        # param_2 = obj.getProduct(k)

    def self_testing(self):
        productOfNumbers = ProductOfNumbers();
        print(productOfNumbers.add(3));        # [3]
        print(productOfNumbers.add(0));        # [3,0]
        print(productOfNumbers.add(2));        # [3,0,2]
        print(productOfNumbers.add(5));        # [3,0,2,5]
        print(productOfNumbers.add(4));        # [3,0,2,5,4]
        print(productOfNumbers.getProduct(2)); # return 20. The product of the last 2 numbers is 5 * 4 = 20
        print(productOfNumbers.getProduct(3)); # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
        print(productOfNumbers.getProduct(4)); # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
        print(productOfNumbers.add(8));        # [3,0,2,5,4,8]
        print(productOfNumbers.getProduct(2)); # return 32. The product of the last 2 numbers is 4 * 8 = 32
        print(productOfNumbers.add(0));        # [3,0,2,5,4,8,0]
        print(productOfNumbers.getProduct(1)); # return 0
        print(productOfNumbers.getProduct(2)); # return 0
        print(productOfNumbers.getProduct(3)); # return 0
        print(productOfNumbers.getProduct(4)); # return 0
        print(productOfNumbers.getProduct(5)); # return 0
        print('===')
        productOfNumbers = ProductOfNumbers();


ProductOfNumbers().self_testing()