class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        ans = [0, 0]
        for i in range(l):
            for j in range(i + 1, l):
                if(nums[i] + nums[j] == target):
                    ans[0] = i
                    ans[1] = j
        return ans