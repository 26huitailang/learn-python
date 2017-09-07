#!/usr/bin/python
# coding: utf-8
from algorithm.sort.basic_sort import *
import pytest
from random import randint
import time
from functools import wraps
import json
from copy import deepcopy

func_time = {}
res = {}


def run_timer(f):
    @wraps(f)
    def function_timer(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        print("\nTotal time running {0}: {1} seconds".format(f.__name__, str(te - ts)))
        func_time[f.__name__] = te - ts
        return result

    return function_timer


@pytest.fixture(scope="module", params=[100, 1000, 10000, 100000, 1000000])
def create_list(request):
    print("start")
    nums = []
    for i in range(request.param):
        nums.append(randint(0, request.param))
    yield nums
    print("end")
    # print(func_time)
    # 用copy赋值，千万不用直接赋值，对func_time的修改会影响前面的结果
    res[request.param] = func_time.copy()
    # print(res)
    jsonObj = json.dumps(res)

    f = open('./logs.json', 'w')
    f.write(jsonObj)
    f.close()


#
# @run_timer
# def test_bubble_sort(create_list):
#     origin_list = create_list.copy()
#     sorted_list = bubble_sort(origin_list)
#     # print(sorted_list, create_list, origin_list)
#     assert sorted_list != create_list
#
#
# @run_timer
# def test_insert_sort(create_list):
#     origin_list = create_list.copy()
#     sorted_list = insert_sort(origin_list)
#     # print(sorted_list, create_list)
#     assert sorted_list != create_list
#
# @run_timer
# def test_select_sort(create_list):
#     origin_list = create_list.copy()
#     sorted_list = select_sort(origin_list)
#     assert sorted_list != create_list


@run_timer
def test_shell_sort_two(create_list):
    origin_list = create_list.copy()
    sorted_list = shell_sort_two(origin_list)
    assert sorted_list != create_list


@run_timer
def test_quick_sort(create_list):
    origin_list = create_list.copy()
    sorted_list = quick_sort(origin_list, 0, len(origin_list) - 1)
    assert sorted_list != create_list


@run_timer
def test_heap_sort(create_list):
    origin_list = create_list.copy()
    heap_sort(origin_list)
    assert origin_list != create_list


@run_timer
def test_merge_sort(create_list):
    origin_list = create_list.copy()
    sorted_list = merge_sort(origin_list)
    assert sorted_list != create_list


@run_timer
def test_radix_sort(create_list):
    origin_list = create_list.copy()
    sorted_list = radix_sort(origin_list)
    assert sorted_list != create_list