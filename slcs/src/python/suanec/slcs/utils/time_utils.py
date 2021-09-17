# !/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'enzhao'
# Created by enzhao on 2021/9/17. 
import time

def time_calc(_func, _retry_times = 1, *args, **kwargs):
    inner_args = [x for x in args]
    inner_kwargs = {k:v for (k,v) in kwargs.items()}
    start_time = time.time()
    for i in xrange(0, _retry_times):
        _func(*inner_args, **inner_kwargs)
    end_time = time.time()
    return _func.__name__ + " : " + str((end_time - start_time)/_retry_times * 1000)
