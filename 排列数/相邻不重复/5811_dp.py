
# https://leetcode-cn.com/problems/painting-a-grid-with-three-different-colors/solution/dong-tai-gui-hua-shuang-bai-jin-gong-can-mlnk/

class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 1000000007
        ans = 0
        typs = set()
        for i1 in range(3):
            if m == 1:
                typs.add((i1,))
                continue
            for i2 in range(3):
                if m == 2:
                    if i1 != i2:
                        typs.add((i1,i2))
                    continue
                for i3 in range(3):
                    if m == 3:
                        if i1 != i2 and i2 != i3:
                            typs.add((i1,i2,i3))
                        continue
                    for i4 in range(3):
                        if m == 4:
                            if i1 != i2 and i2 != i3 and i3 != i4:
                                typs.add((i1,i2,i3,i4))
                            continue
                        for i5 in range(3):
                            if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5:
                                typs.add((i1,i2,i3,i4,i5))
        typs = list(typs)
        typn = len(typs)
        val = [[0] * typn for _ in range(typn)]
        for i in range(typn):
            for j in range(typn):
                flag = True
                for k in range(m):
                    if typs[i][k] == typs[j][k]:
                        flag = False
                val[i][j] = flag
        dp = [[0] * typn for _ in range(n)]
        for i in range(typn):
            dp[0][i] = 1
        for i in range(1,n):
            #status:j=>k
            for j in range(typn):
                for k in range(typn):
                    if val[j][k]:
                        dp[i][k] += dp[i-1][j]
        ans = sum(dp[n-1]) % MOD
        return ans
