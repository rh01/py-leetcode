class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k

        self.nums = sorted(nums, reverse=True)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)

        if len(self.nums) < self.k:
            return self.nums[-1]

        while len(self.nums) != self.k and self.nums != []:
            self.nums.pop()

        return self.nums[-1]
        # return list(reversed(sorted(self.nums.append(val)))).pop()[-1]

