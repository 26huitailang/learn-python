#!/usr/bin/python
# coding: utf-8


def what_are_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_args_and_kwargs()
what_are_args_and_kwargs(1, [2,3], {'a': 'hello'}, name='JJ', age='11')