class Solution:
    def twoSum(self, nums, target):
        my_hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_hashmap:
                return [my_hashmap[diff], i]
            my_hashmap[n] = i
