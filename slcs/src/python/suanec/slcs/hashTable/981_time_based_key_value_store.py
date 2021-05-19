# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/19. 

class TimeMap(object):
    """
    981. Time Based Key-Value Store
    Medium

    1233

    144

    Add to List

    Share
    Create a timebased key-value store class TimeMap, that supports two operations.

    1. set(string key, string value, int timestamp)

    Stores the key and value, along with the given timestamp.
    2. get(string key, int timestamp)

    Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
    If there are multiple such values, it returns the one with the largest timestamp_prev.
    If there are no values, it returns the empty string ("").


    Example 1:

    Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
    Output: [null,null,"bar","bar",null,"bar2","bar2"]
    Explanation:
    TimeMap kv;
    kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
    kv.get("foo", 1);  // output "bar"
    kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
    kv.set("foo", "bar2", 4);
    kv.get("foo", 4); // output "bar2"
    kv.get("foo", 5); //output "bar2"

    Example 2:

    Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    Output: [null,null,null,"","high","high","low","low"]


    Note:

    All key/value strings are lowercase.
    All key/value strings have length in the range [1, 100]
    The timestamps for all TimeMap.set operations are strictly increasing.
    1 <= timestamp <= 10^7
    TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.

    """

    def __init__(self):
        """
        Runtime: 592 ms, faster than 91.71% of Python online submissions for Time Based Key-Value Store.
        Memory Usage: 67.1 MB, less than 97.59% of Python online submissions for Time Based Key-Value Store.

        Initialize your data structure here.
        """
        self.inner_dict = {} # key : (timestamp_list, value_list)


    def binary_search_less_max(self, _list, _target):
        if(len(_list) < 1):
            return -1
        if(len(_list) < 2):
            if(_list[0] <= _target):
                return 0
            else:
                return -1
        low = 0
        high = len(_list) - 1
        mid = high >> 1
        while(low < high):
            if(_list[mid] == _target):
                return mid
            elif(_list[mid] > _target):
                high = mid - 1
                mid = ((high - low) >> 1) + low
            else:
                low = mid + 1
                mid = ((high - low) >> 1) + low
        if(_list[mid] <= _target):
            return mid
        elif(_list[mid] > _target):
            if(mid == 0):
                return mid
            else:
                if(_list[mid-1] <= _target): return mid-1
                else: return mid

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        (time_list, value_list) = self.inner_dict.get(key, ([],[]))
        time_list.append(timestamp)
        value_list.append(value)
        self.inner_dict[key] = (time_list, value_list)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        (time_list, value_list) = self.inner_dict.get(key, ([],[]))
        if(len(time_list) < 1):
            return ""
        if(timestamp < time_list[0]):
            return ""
        if(timestamp > time_list[-1]):
            return value_list[-1]
        timestamp_index = self.binary_search_less_max(time_list, timestamp)
        return value_list[timestamp_index]


        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)

    def self_testing(self):
        l = [1,2,4,6,9,10,12]
        # 4
        t = 9
        print(self.binary_search_less_max(l, t))
        # 3
        t = 8
        print(self.binary_search_less_max(l, t))
        kv = TimeMap()
        kv.set("foo", "bar", 1);
        assert "bar" == kv.get("foo", 1);
        assert "bar" == kv.get("foo", 3);
        kv.set("foo", "bar2", 4);
        assert "bar2" == kv.get("foo", 4);
        assert "bar2" == kv.get("foo", 5);
        kv = TimeMap()
        kv.set("love","high",10)
        kv.set("love","low",20)
        assert "" == kv.get("love",5)
        assert "high" == kv.get("love",10)
        assert "high" == kv.get("love",15)
        assert "low" == kv.get("love",20)
        assert "low" == kv.get("love",25)



TimeMap().self_testing()
