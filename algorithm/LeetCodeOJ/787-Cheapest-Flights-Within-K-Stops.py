class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # 将节点u能到达的节点归类，方便后面探索
        # 这里索引就是编号，如果是其他的也可以用字典处理
        graph = [[] for _ in range(n)]
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        queue = [(src, -1, 0)]  # 将源节点放入队列，以便开始搜索，点/步数/花费
        min_price = 1e9  # 初始化一个最大值
        while queue:
            u, step, cost = queue.pop(0)  # BFS是FIFO的，所以弹出第一个节点
            # 如果u就是目标点，且价格小于现在的最小值
            # 就跳过，这个时候queue为空，min_price为0，结束
            if u == dst and min_price > cost:
                min_price = cost
                continue
            
            # 如果还没到就访问他的子节点
            for next, price in graph[u]:
                # 下一节点价格满足且中间步数满足
                if cost + price < min_price and step + 1 <= K:
                    # 添加到队列里面，灰色
                    queue.append((next, step + 1, cost + price))

        # 直到搜索了所有满足条件的点后
        return min_price if min_price < 1e9 else -1
