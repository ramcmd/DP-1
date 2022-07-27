#TC: O(n) where n is the number of houses
#SC: O(n) because we are creating a dp array of len n 

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = []
        dp.append(nums[0])
        if len(nums) == 1:
            return dp[-1]
        else:
            dp.append(max(nums[0], nums[1]))
        
        for i in range(2, len(nums)):
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        
        return dp[-1]