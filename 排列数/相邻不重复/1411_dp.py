class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        fi0, fi1 = 6, 6
        for i in range(2, n + 1):
            fi0, fi1 = (2 * fi0 + 2 * fi1) % mod, (2 * fi0 + 3 * fi1) % mod
        return (fi0 + fi1) % mod

# https://leetcode-cn.com/problems/number-of-ways-to-paint-n-3-grid/solution/gei-n-x-3-wang-ge-tu-tu-se-de-fang-an-shu-by-leetc/
