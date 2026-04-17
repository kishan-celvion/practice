class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(x):
            return int(str(x)[::-1])
        index_map = {}
        min_dist = float('inf')
        for i in range(len(nums)):
            rev = reverse(nums[i])
            if rev in index_map:
                min_dist = min(min_dist, i - index_map[rev])
            index_map[nums[i]] = i
        return -1 if min_dist == float('inf') else min_dist

obj = Solution()
print(obj.minMirrorPairDistance())