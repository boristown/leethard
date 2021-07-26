class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        pos = {}
        for i,t in enumerate(target):
            pos[t] = i

        d = []
        for val in arr:
            if val in pos:
                idx = pos[val]
                site = bisect.bisect_left(d, idx)
                if site < len(d):
                    d[site] = idx
                else:
                    d.append(idx)
        
        return n-len(d)
      
 #https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/solution/de-dao-zi-xu-lie-de-zui-shao-cao-zuo-ci-hefgl/
