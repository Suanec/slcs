# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/19. 

class Solution(object):
    """
    406. Queue Reconstruction by Height
    Medium

    4058

    450

    Add to List

    Share
    You are given an array of people, people,
    which are the attributes of some people in a queue (not necessarily in order).
    Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front
    who have a height greater than or equal to hi.

    Reconstruct and return the queue that is represented by the input array people.
    The returned queue should be formatted as an array queue,
    where queue[j] = [hj, kj] is the attributes of the jth person in the queue
    (queue[0] is the person at the front of the queue).



    Example 1:

    Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    [[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]]
    Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    Explanation:
    Person 0 has height 5 with no other people taller or the same height in front.
    Person 1 has height 7 with no other people taller or the same height in front.
    Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
    Person 3 has height 6 with one person taller or the same height in front, which is person 1.
    Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
    Person 5 has height 7 with one person taller or the same height in front, which is person 1.
    Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
    Example 2:

    Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]


    Constraints:

    1 <= people.length <= 2000
    0 <= hi <= 106
    0 <= ki < people.length
    It is guaranteed that the queue can be reconstructed.

    What can you say about the position of the shortest person?
    If the position of the shortest person is i, how many people would be in front of the shortest person?
    Once you fix the position of the shortest person, what can you say about the position of the second shortest person?
    """
    def reconstructQueue(self, people):
        """
        Runtime: 72 ms, faster than 92.44% of Python online submissions for Queue Reconstruction by Height.
        Memory Usage: 13.9 MB, less than 72.89% of Python online submissions for Queue Reconstruction by Height.
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if(len(people) == 1):
            return people
        rst_people = []
        self.people_height_memo = {}
        self.height_max_index = {}
        for person in people:
            (height, count) = person
            self.people_height_memo[height] = self.people_height_memo.get(height, [])
            self.people_height_memo[height].append(person)
        self.height_sorted = sorted(self.people_height_memo.keys(), reverse=True)

        for height in self.height_sorted:
            person_list = sorted( self.people_height_memo[height] , key=lambda x : x[1])
            if(len(rst_people) == 0):
                for person in person_list:
                    rst_people.append(person)
            else:
                for person in person_list:
                    (_, count) = person
                    rst_people.insert(count, person)
        return rst_people

    def self_testing(self):
        # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        print(self.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
        # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
        print(self.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))

Solution().self_testing()
