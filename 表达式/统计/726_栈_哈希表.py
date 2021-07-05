class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        c = {}
        s = [1]
        f = formula
        n = len(f)
        i = n-1
        num = 1
        def get_num(f,i):
            nm = int(f[i])
            times = 0
            i -= 1
            while i >= 0:
                if '0' <= f[i] <=  '9':
                    times += 1
                    nm += 10 ** times * int(f[i])
                    i -= 1
                else:
                    break
            return i,nm
        def get_ele(f,i):
            ele = f[i]
            i -= 1
            while i >= 0:
                if 'a' <= f[i] <=  'z':
                    ele = f[i] + ele
                    i -= 1
                elif 'A' <= f[i] <=  'Z':
                    ele = f[i] + ele
                    i -= 1
                    break
            return i,ele

        def add_ele(c,ele,last,num):
            if ele not in c:
                c[ele] = last * num
            else:
                c[ele] += last * num

        while i >= 0:
            if '0' <= f[i] <=  '9':
                i,num = get_num(f,i)
            elif 'a' <= f[i] <= 'z':
                i,ele = get_ele(f,i)
                add_ele(c,ele,s[-1],num)
                num = 1
            elif 'A' <= f[i] <= 'Z':
                i,ele = i-1,f[i]
                add_ele(c,ele,s[-1],num)
                num = 1
            elif f[i] == ')':
                s.append(s[-1]*num)
                num = 1
                i-=1
            elif f[i] == '(':
                s.pop()
                i-=1
            
        ans = ''
        c = c.items()
        c.sort()
        for k,v in c:
            if v > 1:
                ans = ans + k + str(v)
            else:
                ans = ans + k
        return ans
      
#https://leetcode-cn.com/problems/number-of-atoms/
