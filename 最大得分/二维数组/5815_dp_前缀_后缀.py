class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])
        dp1 = [0] * n
        dp2 = [0] * n
        for i in range(m):
            dp1,dp2 = dp2,dp1
            pre = [0] * (n+1)
            suf = [0] * n
            mx = -inf
            for j in range(n):
                mx = max(mx,dp1[j]+j)
                pre[j+1] = mx
            mx = -inf
            for j in range(n-1,-1,-1):
                mx = max(mx,dp1[j]-j)
                suf[j] = mx
            for j in range(n):
                lk = pre[j]-j
                rk = suf[j]+j
                dp2[j] = max(lk,rk) + points[i][j]
        return max(dp2)
      
 #https://leetcode-cn.com/problems/maximum-number-of-points-with-cost/submissions/
