class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        heapset= set()
        for n in nums:
            if n in heapset:
                return True
            heapset.add(n)
        return False