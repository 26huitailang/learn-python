#!/usr/bin/python
# coding: utf-8
from algorithm.sort.basicSort import *
import pytest
from random import randint
import time
from functools import wraps


def run_timer(f):
    @wraps(f)
    def function_timer(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        print("\nTotal time running {0}: {1} seconds".format(f.__name__, str(te - ts)))
        return result

    return function_timer


@pytest.fixture(scope="module", params=[100, 1000, 10000])
def create_list(request):
    nums = []
    for i in range(request.param):
        nums.append(randint(0, request.param))
    return nums


@run_timer
def test_bubble_sort(create_list):
    origin_list = create_list.copy()
    sort_list = bubble_sort(origin_list)
    # print(sort_list, create_list, origin_list)
    assert sort_list != create_list


@run_timer
def test_insert_sort(create_list):
    origin_list = create_list.copy()
    sort_list = insert_sort(origin_list)
    # print(sort_list, create_list)
    assert sort_list != create_list
