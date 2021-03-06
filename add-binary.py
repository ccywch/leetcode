# -*- coding: utf-8 -*-
#author: Chen Chunyang

#Description:
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}

    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]