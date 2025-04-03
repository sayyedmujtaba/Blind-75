class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer = []
        
        for i, x in enumerate(nums[:-2]):
            if i and x == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                s = x + nums[l] + nums[r]
                
                if not s:
                    answer.append([x, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1  
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l, r = l + 1, r - 1
                elif s < 0: l += 1
                else: r -= 1
                    
        return answer