#! usr/bin/python
# coding: utf-8

from xmlrpclib import ServerProxy, Fault
from server import Node, UNHANDLED
from client import randomString
from threading import Thread
from time import sleep
from os import listdir
import sys
import wx

HEAD_START = 0.1  # Seconds
SECRET_LENGTH = 100

class Client(wx.App):
    """
    主client类，用于设定GUI，启动为文件服务的Node