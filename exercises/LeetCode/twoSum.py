class Solution(object):
    def twoSum(self, nums, target):
        for n1 in range(len(nums)):
           for n2 in range(n1 +1, len(nums), 1):
                if nums[n1] + nums[n2] == target:
                    sumList = [n1, n2]
        return sumList
        
exercise = Solution()
print(exercise.twoSum([3,2,4], 6))