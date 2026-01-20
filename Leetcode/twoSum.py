"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. 
You can return the answer in any order."""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(nums)>=2):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i]+nums[j]==target:
                        return [i,j]
            return []
        
sol = Solution()
nums=[]
n_size = int(input("Enter the number of elements: "))
for i in range(n_size):
    element = int(input("Enter element = "))
    nums.append(element)
target = int(input("Enter the target element: "))
print(sol.twoSum(nums, target))
    