# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/4/27. 

class RandomizedCollection(object):
    """
    381. Insert Delete GetRandom O(1) - Duplicates allowed
    Hard

    1133

    90

    Add to List

    Share
    Implement the RandomizedCollection class:

    RandomizedCollection() Initializes the RandomizedCollection object.
    bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
    int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.


    Example 1:

    Input
    ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
    [[], [1], [1], [2], [], [1], []]
    Output
    [null, true, false, true, 2, true, 1]

    Explanation
    RandomizedCollection randomizedCollection = new RandomizedCollection();
    randomizedCollection.insert(1);   // return True. Inserts 1 to the collection. Returns true as the collection did not contain 1.
    randomizedCollection.insert(1);   // return False. Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
    randomizedCollection.insert(2);   // return True. Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
    randomizedCollection.getRandom(); // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
    randomizedCollection.remove(1);   // return True. Removes 1 from the collection, returns true. Collection now contains [1,2].
    randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equally likely.


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
        self.inner_list.append(val)
        self.val_idx_set = self.idx_memo.get(val, set())
        if(len(self.val_idx_set) > 0):
            rst = False
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
        obj = RandomizedCollection()
        print(obj.insert(1))
        print(obj.insert(1))
        print(obj.insert(2))
        print(obj.getRandom())
        print(obj.remove(1))
        print(obj.getRandom())
        obj = RandomizedCollection()
        # ["RandomizedCollection","insert","insert","remove","insert","remove","getRandom"]
        # [[],[0],[1],[0],[2],[1],[]]

        # [null,true,true,true,true,true,1]
        # Expected
        # [null,true,true,true,true,true,2]
        print(obj.insert(0))
        print(obj.insert(1))
        print(obj.remove(0))
        print(obj.insert(2))
        print(obj.remove(1))
        print(obj.getRandom())

        obj = RandomizedCollection()
        # ["RandomizedCollection","insert","remove","insert"]
        # [[],[1],[1],[1]]
        print(obj.insert(1))
        print(obj.remove(2))
        print(obj.remove(1))
        print(obj.insert(1))

        obj = RandomizedCollection()
        # ["RandomizedCollection","insert","insert","insert","insert","insert","insert","insert","insert","insert","remove","remove"]
        # [[],[1],[0],[1],[1],[1],[1],[1],[1],[0],[0],[0]]
        print(obj.insert(1))
        print(obj.insert(0))
        print(obj.insert(1))
        print(obj.insert(1))
        print(obj.insert(1))
        print(obj.insert(1))
        print(obj.insert(1))
        print(obj.insert(1))
        print(obj.insert(0))
        print(obj.remove(0))
        print(obj.remove(0))



RandomizedCollection().self_testing()