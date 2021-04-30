# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/4/28.

class RandomizedSet(object):
    """
    Runtime: 104 ms, faster than 43.09% of Python online submissions for Insert Delete GetRandom O(1).
    Memory Usage: 19.7 MB, less than 7.77% of Python online submissions for Insert Delete GetRandom O(1).
    380. Insert Delete GetRandom O(1)
    Medium

    3539

    206

    Add to List

    Share
    Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.


    Example 1:

    Input
    ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    [[], [1], [2], [2], [], [1], [2], []]
    Output
    [null, true, false, true, 2, true, false, 2]

    Explanation
    RandomizedSet randomizedSet = new RandomizedSet();
    randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully. \
        randomizedSet.remove(2); // Returns false as 2 does not exist in the set. \
        randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2]. \
        randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
    randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.insert(2); // 2 was already in the set, so return false.
    randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


    Constraints:

    -231 <= val <= 231 - 1
    At most 105 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.


    Follow up: Could you implement the functions of the class with each function works in average O(1) time?
    """
    def __init__(self):
        """
        Runtime: 108 ms, faster than 25.00% of Python online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.
        Memory Usage: 19.4 MB, less than 50.00% of Python online submissions for Insert Delete GetRandom O(1) - Duplicates allowed.

        Initialize your data structure here.
        """
        self.inner_list = []
        self.idx_memo = {}
        import random
        self.rander = random.Random()


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        rst = True
        self.val_idx_set = self.idx_memo.get(val, set())
        if(len(self.val_idx_set) > 0):
            rst = False
        else:
            self.inner_list.append(val)
            self.val_idx_set.add(len(self.inner_list) - 1)
        self.idx_memo[val] = self.val_idx_set
        return rst


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        rst = True
        self.val_idx_set = self.idx_memo.get(val, set())
        if(len(self.inner_list) == 1):
            if(val == self.inner_list[0]):
                self.idx_memo.clear()
                self.inner_list = []
                return rst
            else:
                rst = False
                return rst
        if(len(self.val_idx_set) > 0):
            self.remove_idx = self.val_idx_set.pop()
            max_idx_inner_list = len(self.inner_list) - 1
            if(max_idx_inner_list in self.idx_memo[self.inner_list[max_idx_inner_list]]):
                self.idx_memo[self.inner_list[max_idx_inner_list]].remove(max_idx_inner_list)
            if(self.remove_idx != max_idx_inner_list):
                self.idx_memo[self.inner_list[max_idx_inner_list]].add(self.remove_idx)
                self.inner_list[self.remove_idx] = self.inner_list[max_idx_inner_list]
            self.inner_list.pop(max_idx_inner_list)
        else:
            rst = False
        return rst

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        rand_idx = self.rander.randrange(0, len(self.inner_list))
        return self.inner_list[rand_idx]

        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()

    def self_testing(self):
        obj = RandomizedSet()
        # ["RandomizedSet","insert","insert","getRandom","getRandom","insert","remove","getRandom","getRandom","insert","remove"]
        # [[],[3],[3],[],[],[1],[3],[],[],[0],[0]]
        # Output
        # [null,true,false,3,3,true,true,3,3,true,true]
        # Expected
        # [null,true,false,3,3,true,true,1,1,true,true]
        print(obj.insert(3))
        print(obj.insert(3))
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.insert(1))
        print(obj.remove(3))
        print(obj.getRandom())
        print(obj.getRandom())
        print(obj.insert(0))
        print(obj.remove(0))

RandomizedSet().self_testing()
