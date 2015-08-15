# -*- coding: utf-8 -*-
#Author: Chen Chunyang
'''
Question description:
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


#The time complexity of this solution is O(n)
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        nums_dic = {}
        for num in nums:
            if num in nums_dic:
                nums_dic[num] = nums_dic[num] + 1
            else:
                nums_dic[num] = 1
        #nums_set = set(nums)
        for num in nums:
            if (target-num) in nums_dic:
                #For cases in which two elements are not equal
                if target-num != num:
                    return sorted([nums.index(num)+1,nums.index(target-num)+1])
                #For cases in which the two elements are equal
                elif nums_dic[num]>1:
                    order = []
                    for i in xrange(len(nums)):
                        if len(order) == 2:
                            break
                        if nums[i] == num:
                            order.append(i+1)
                    return [order[0], order[1]]