#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
#
'''Solution1 time complexity is N^2 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = []
        flage = False
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
'''

#solution2 using hashmap (one pass)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[nums[i]]= i 
'''

#solution3 using hashmap 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range (len(nums)):
            hashmap[nums[i]]= i
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!=i:
                return [i,hashmap[complement]]        
# @lc code=end

