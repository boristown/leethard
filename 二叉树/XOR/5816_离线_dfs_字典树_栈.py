class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        graph=collections.defaultdict(list)
        n=len(parents)
        # 建树及寻找根节点
        root=-1
        for i,p in enumerate(parents):
            graph[p].append(i)
            if p==-1:
                root=i
                
        N=(n+1)*19
        trie=[[0]*2 for _ in range(N)]
        cnt=[0]*N
        self.idx=0
        # 插入字典树，v为1时插入节点，v为-1时删除节点
        def insert(x, v):
            p = 0
            for i in range(18, -1, -1):
                u = x >> i & 1
                if trie[p][u] == 0:
                    self.idx += 1
                    trie[p][u] = self.idx
                p = trie[p][u]
                cnt[p] += v
        # 查询字典树
        def query(x):
            res = p = 0
            for i in range(18, -1, -1):
                u = x >> i & 1
                if cnt[trie[p][1-u]]:
                    p = trie[p][1-u]
                    res = res * 2 + 1
                else:
                    p = trie[p][u]
                    res = res * 2
            return res            
                  
        # 将每个点对应的索引和值存入哈希表   
        st=collections.defaultdict(list)
        for i,(r,v) in enumerate(queries):
            st[r].append([v,i])
        
        stack=[]
        res=[0]*len(queries)
        
        # 先序遍历，stack中仅仅存储根节点到当前节点的路径
        def dfs(root):
            stack.append(root)
            insert(root,1)
            if root in st:
                for v,i in st[root]:
                    ans=query(v)
                    res[i]=ans
            
            for son in graph[root]:
                dfs(son)
                
            node=stack.pop()
            insert(node,-1)
            
        
        dfs(root)
        return res
        

#作者：yim-6
#链接：https://leetcode-cn.com/problems/maximum-genetic-difference-query/solution/python3-chi-xian-dfszi-dian-shu-zhan-by-na5er/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
