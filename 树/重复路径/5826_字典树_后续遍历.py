#https://leetcode-cn.com/problems/delete-duplicate-folders-in-system/

class Trie:
    # 当前节点结构的序列化表示
    serial: str = ""
    # 当前节点的子节点
    children: dict

    def __init__(self):
        self.children = dict()

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 根节点
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        # 哈希表记录每一种序列化表示的出现次数
        freq = Counter()
        # 基于深度优先搜索的后序遍历，计算每一个节点结构的序列化表示
        def construct(node: Trie) -> None:
            # 如果是叶节点，那么序列化表示为空字符串，无需进行任何操作
            if not node.children:
                return

            v = list()
            # 如果不是叶节点，需要先计算子节点结构的序列化表示
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")
            
            # 防止顺序的问题，需要进行排序
            v.sort()
            node.serial = "".join(v)
            # 计入哈希表
            freq[node.serial] += 1

        construct(root)

        ans = list()
        # 记录根节点到当前节点的路径
        path = list()

        def operate(node: Trie) -> None:
            # 如果序列化表示在哈希表中出现了超过 1 次，就需要删除
            if freq[node.serial] > 1:
                return
            # 否则将路径加入答案
            if path:
                ans.append(path[:])

            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        operate(root)
        return ans

#作者：LeetCode-Solution
#链接：https://leetcode-cn.com/problems/delete-duplicate-folders-in-system/solution/shan-chu-xi-tong-zhong-de-zhong-fu-wen-j-ic32/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
