class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):       # taking len(nums) as we are starting from 1 not 0
            nums[i] += nums[i - 1]          # adding previously calculated sum to new element of array
        return nums    