class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        Q = collections.deque()
        #维护结果数组
        res = [0 for _ in range(n)] 
        #从右向左遍历
        for i in range(n-1 , -1, -1): 
            #如果当前高度比队列左端的高，则从左端弹出队列中的高度，且可以看到的人数+1
            while Q and heights[i] > Q[0]: 
                Q.popleft()
                res[i] += 1
            #队列不为空则可以看到的人数+1
            if Q:
                res[i] += 1
            #当前高度压入队列左端
            Q.appendleft(heights[i])
        return res
 
#https://leetcode-cn.com/problems/number-of-visible-people-in-a-queue/
