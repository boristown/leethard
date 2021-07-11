#两边和同时减少到一边为0，两边问号同时减少到一边没有问号。
#这样下来只有一边有数，只有一边有问号 (只有一种特殊情况就是两边数字和问号个数都为0，这样只能false)。
#且数字问号不能再同一边， 且问号必须是双的。不然都是true
#数字 必须等于 问号个数 /2 * 9 不然都是true;
class Solution:
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        m = num.count('?')
        if m % 2 == 1:
            return True
        p = num[:n//2].count('?')
        q = num[n//2:].count('?')
        sm1 = 0
        sm2 = 0
        for i in num[:n//2]:
            if i != '?':
                sm1 += int(i)
        for i in num[n//2:]:
            if i != '?':
                sm2 += int(i)
        n1 = abs(p - q)
        n2 = abs(sm1 - sm2)
        if (n1 // 2) * 9 == n2:
            return False
        return True
