class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # 根据正文部分的分析，我们选择的 mod 需要远大于 10^10
        # Python 直接选择 10^9+7 * 10^9+9 作为模数即可
        # 乘积约为 10^18，远大于 10^10
        mod = (10**9 + 7) * (10**9 + 9)

        # 本题中数组元素的范围为 [0, 10^5]
        # 因此我们在 [10^6, 10^7] 的范围内随机选取进制 base
        base = random.randint(10**6, 10**7)
        
        m = len(paths)
        # 确定二分查找的上下界
        left, right, ans = 1, len(min(paths, key=lambda p: len(p))), 0
        while left <= right:
            length = (left + right) // 2
            mult = pow(base, length, mod)
            s = set()
            check = True

            for i in range(m):
                hashvalue = 0
                # 计算首个长度为 len 的子数组的哈希值
                for j in range(length):
                    hashvalue = (hashvalue * base + paths[i][j]) % mod

                t = set()
                # 如果我们遍历的是第 0 个数组，或者上一个数组的哈希表中包含该哈希值
                # 我们才会将哈希值加入当前数组的哈希表中
                if i == 0 or hashvalue in s:
                    t.add(hashvalue)
                # 递推计算后续子数组的哈希值
                for j in range(length, len(paths[i])):
                    hashvalue = (hashvalue * base - paths[i][j - length] * mult + paths[i][j]) % mod
                    if i == 0 or hashvalue in s:
                        t.add(hashvalue)
                if not t:
                    check = False
                    break
                s = t
            
            if check:
                ans = length
                left = length + 1
            else:
                right = length - 1
        
        return ans
