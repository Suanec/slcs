# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/5/17. 

class Solution(object):
    """
    310. Minimum Height Trees
    Medium

    3104

    138

    Add to List

    Share
    A tree is an undirected graph in which any two vertices are connected by exactly one path.
    In other words, any connected graph without simple cycles is a tree.

    Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
    where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree,
    you can choose any node of the tree as the root.
    When you select a node x as the root, the result tree has height h.
    Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

    Return a list of all MHTs' root labels. You can return the answer in any order.

    The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

    Example 1:


    Input: n = 4, edges = [[1,0],[1,2],[1,3]]
    Output: [1]
    Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
    Example 2:


    Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    Output: [3,4]
    Example 3:

    Input: n = 1, edges = []
    Output: [0]
    Example 4:

    Input: n = 2, edges = [[0,1]]
    Output: [0,1]


    Constraints:

    1 <= n <= 2 * 104
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    All the pairs (ai, bi) are distinct.
    The given input is guaranteed to be a tree and there will be no repeated edges.

    ----
    First let's review some statement for tree in graph theory:

    (1) A tree is an undirected graph in which any two vertices are
    connected by exactly one path.

    (2) Any connected graph who has n nodes with n-1 edges is a tree.

    (3) The degree of a vertex of a graph is the number of
    edges incident to the vertex.

    (4) A leaf is a vertex of degree 1. An internal vertex is a vertex of
    degree at least 2.

    (5) A path graph is a tree with two or more vertices that is not
    branched at all.

    (6) A tree is called a rooted tree if one vertex has been designated
    the root.

    (7) The height of a rooted tree is the number of edges on the longest
    downward path between root and a leaf.

    OK. Let's stop here and look at our problem.

    Our problem want us to find the minimum height trees and return their root labels.

    First we can think about a simple case -- a path graph.

    For a path graph of n nodes, find the minimum height trees is trivial.

    Just designate the middle point(s) as roots.

    Despite its triviality, let design a algorithm to find them.

    Suppose we don't know n, nor do we have random access of the nodes.

    We have to traversal.

    It is very easy to get the idea of two pointers.

    One from each end and move at the same speed.

    When they meet or they are one step away, (depends on the parity of n), we have the roots we want.

    This gives us a lot of useful ideas to crack our real problem.

    For a tree we can do some thing similar.

    We start from every end, by end we mean vertex of degree 1 (aka leaves).

    We let the pointers move the same speed.

    When two pointers meet, we keep only one of them, until the last two pointers meet or one step away we then find the roots.

    It is easy to see that the last two pointers are from the two ends of the longest path in the graph.

    The actual implementation is similar to the BFS topological sort.

    Remove the leaves, update the degrees of inner vertexes.

    Then remove the new leaves. Doing so level by level until there are 2 or 1 nodes left. What's left is our answer!

    The time complexity and space complexity are both O(n).

    Note that for a tree we always have V = n, E = n-1.

    Hint:

    How many MHTs can a graph have at most?


    """
    # Python

    def findMinHeightTrees_discuss(self, n, edges):
        """
        Runtime: 184 ms, faster than 99.64% of Python online submissions for Minimum Height Trees.
        Memory Usage: 18.9 MB, less than 67.39% of Python online submissions for Minimum Height Trees.

        Runtime: 196 ms, faster than 86.59% of Python online submissions for Minimum Height Trees.
        Memory Usage: 19 MB, less than 64.49% of Python online submissions for Minimum Height Trees.


        Java

        public List<Integer> findMinHeightTrees(int n, int[][] edges) {
            if (n == 1) return Collections.singletonList(0);

            List<Set<Integer>> adj = new ArrayList<>(n);
            for (int i = 0; i < n; ++i) adj.add(new HashSet<>());
            for (int[] edge : edges) {
                adj.get(edge[0]).add(edge[1]);
                adj.get(edge[1]).add(edge[0]);
            }

            List<Integer> leaves = new ArrayList<>();
            for (int i = 0; i < n; ++i)
            if (adj.get(i).size() == 1) leaves.add(i);

            while (n > 2) {
                n -= leaves.size();
                List<Integer> newLeaves = new ArrayList<>();
                for (int i : leaves) {
                    int j = adj.get(i).iterator().next();
                    adj.get(j).remove(i);
                    if (adj.get(j).size() == 1) newLeaves.add(j);
                }
                leaves = newLeaves;
            }
            return leaves;
        }

       // Runtime: 53 ms

        :param n:
        :param edges:
        :return:
        """
        if n == 1: return [0]
        adj = [set() for _ in xrange(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in xrange(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves
        # Runtime : 104ms

    def findMinHeightTrees(self, n, edges):
        return self.findMinHeightTrees_self(n, edges)
        # return self.findMinHeightTrees_discuss(n, edges)
        # return self.findMinHeightTrees_construct(n, edges)

    def findMinHeightTrees_self(self, n, edges):
        """
        Runtime: 184 ms, faster than 99.64% of Python online submissions for Minimum Height Trees.
        Memory Usage: 19 MB, less than 64.49% of Python online submissions for Minimum Height Trees.
        :param n:
        :param edges:
        :return:
        """
        if(n == 1):
            return [0]
        if(n == 2):
            return [0,1]

        self.edges_memo = [set() for x in xrange(n)]
        for (i,j) in edges:
            self.edges_memo[i].add(j)
            self.edges_memo[j].add(i)

        leaves = [ x for x in xrange(0,n) if 1 == len(self.edges_memo[x]) ]

        inner_n = n
        while inner_n > 2:
            inner_n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = self.edges_memo[i].pop()
                self.edges_memo[j].remove(i)
                if(len(self.edges_memo[j]) == 1):
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves

    def findMinHeightTrees_construct(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if(n == 1):
            return [0]
        if(n == 2):
            return [0,1]

        self.height_root_memo = {}
        self.degree = [0] * n
        self.edges_memo = {}
        self.node_depth_memo = {}
        for (i,j) in edges:
            self.degree[i] += 1
            self.degree[j] += 1
            self.edges_memo[i] = self.edges_memo.get(i, set())
            self.edges_memo[i].add(j)
            self.edges_memo[j] = self.edges_memo.get(j, set())
            self.edges_memo[j].add(i)
        self.degree_index = [[idx, item] for [idx, item] in enumerate(self.degree) ]
        return list(self.construct_trees(n, edges))

    def construct_trees(self, n, edges):
        for i in xrange(0, n):
            height = self.construct_tree(i, edges)

            self.height_root_memo[height] = self.height_root_memo.get(height, set())
            self.height_root_memo[height].add(i)
        min_height_root_set = min(self.height_root_memo.keys())
        return self.height_root_memo.get(min_height_root_set)

    def construct_tree(self, start_node, edges):
        queue = []
        seen_node = set()
        start_entry = (start_node, 1)
        queue.append(start_entry)
        max_depth = 1
        while(len(queue) > 0):
            (cur_node, cur_level) = queue.pop(0)
            seen_node.add(cur_node)
            if(cur_level > max_depth):
                max_depth = cur_level
            for node in self.edges_memo[cur_node]:
                if(node not in seen_node):
                    next_entry = (node, cur_level + 1)
                    queue.append(next_entry)
        return max_depth

    def self_testing(self):
        # [0, 1]
        print(self.findMinHeightTrees(2, [[0,1]]))
        # [0]
        print(self.findMinHeightTrees(1, []))
        # [1]
        print(self.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
        # [3, 4]
        print(self.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))

Solution().self_testing()
