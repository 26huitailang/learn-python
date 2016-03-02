#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'peter'

from nose.tools import *
from ex48 import parser

word_list = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')]

def test_peek():
    assert_equal(parser.peek(word_list), 'noun')

def test_match():
    assert_equal(parser.match(word_list, 'noun'),( 'noun', 'bear'))

def test_skip():
    assert_equal(parser.skip(word_list, 'noun'), None)

def test_parse_verb():
    # 确保parser.parse_verb([('noun', 'dog')])，一定会抛出ParserError来，否则测试失败，如'verb'
    assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'dog')])

def test_parse_object():
    # 传入'noun'或者'direction'测试不通过
    assert_raises(parser.ParserError, parser.parse_object, [('verb', 'dog')])
    assert_raises(parser.ParserError, parser.parse_object, [('stop', 'dog')])

def test_parse_subject():
    assert_raises(parser.ParserError, parser.parse_subject, [('stop', 'dog')])




