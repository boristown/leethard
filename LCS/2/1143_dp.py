#https://leetcode-cn.com/leetbook/read/dynamic-programming-1-plus/5pkl9m/

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        N = len(t1)
        M = len(t2)
        # dp[i][j] t1 中 0~N 和 t2 中 0~M 的最长子序列的长度
        # dp[i][j] = dp[i-1][j-1] + 1 if t1[i] == t2[j] else max(dp[i-1][j],dp[i][j-1])
        dp = [[0] * (M+1) for _ in range(N+1)]
        for i in range(N):
            for j in range(M):
                dp[i+1][j+1]=dp[i][j]+1 if t1[i]==t2[j] else max(dp[i][j+1],dp[i+1][j])
        return dp[N][M]

#作者：smile
#链接：https://leetcode-cn.com/leetbook/read/dynamic-programming-1-plus/5pkl9m/?discussion=mC1VwD
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
