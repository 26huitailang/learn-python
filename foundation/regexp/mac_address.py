"""
匹配大小写的MAC地址
"""
# coding=utf-8

import re


def isValidIp(ip):
    if re.match(r"^\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*$", ip):
        return True
    return False


def isValidMac(mac: str):
    if re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", mac):
        return True
    return False


if __name__ == "__main__":
    assert isValidMac("BC:5F:F4:6B:3E:6F") is True
    assert isValidMac("BC:F:F4:6B:3E:6F") is False
    assert isValidIp("192.168.2.105") is True
    assert isValidIp(".168.2.105") is False
