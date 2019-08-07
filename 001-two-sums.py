class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_map = dict()
        for idx, num in enumerate(nums):
            if target - num in hash_map:
                return [idx, hash_map[target - num]]
            hash_map[num] = idx

    def twoSumBrute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pass

