class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for m in nums:
            p=bisect.bisect_left(dp,m)
            if p==len(dp): dp.append(m)
            else: dp[p]=m
        return len(dp)

#作者：tang-bo-o
#链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/pythontan-xin-er-fen-cha-zhao-6xing-gao-yrarn/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
