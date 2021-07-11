class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        f = [[float("inf")] * n for _ in range(maxTime + 1)]
        #f[t][i]表示在时间t到达城市i的费用
        f[0][0] = passingFees[0]
        #因为道路是双向的，所以先考虑从i到j的情况，再考虑从j到i的情况
        #f[t][i] = min(f[t][i],f[t-cost][j] + fee[i])
        #f[t][j] = min(f[t][j],f[t-cost][i] + fee[j])
        for t in range(1, maxTime + 1):
            for i, j, cost in edges:
                if cost <= t:
                    f[t][i] = min(f[t][i], f[t - cost][j] + passingFees[i])
                    f[t][j] = min(f[t][j], f[t - cost][i] + passingFees[j])
        
        ans = min(f[t][n - 1] for t in range(1, maxTime + 1))
        return -1 if ans == float("inf") else ans

#https://leetcode-cn.com/problems/minimum-cost-to-reach-destination-in-time/
