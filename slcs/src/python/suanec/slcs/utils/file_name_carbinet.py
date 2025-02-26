# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2025/2/26.

def file_name_generator(_problem_name = "[442]Find All Duplicates in an Array.py"):
    # 442_find_all_duplicates_in_an_array.py
    rst = _problem_name.lower()
    rst = rst.replace(" ", "_")
    rst = rst.replace("[", "")
    rst = rst.replace("]", "_")
    print(rst)

if __name__ == '__main__':
    file_name_generator("[442]Find All Duplicates in an Array.py")