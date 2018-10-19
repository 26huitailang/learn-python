"""
最大子数列问题 https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98
扫描一次数列，计算每个扫描点以该店为终点的子数列最大和
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 更低的买入，更高的卖出
        if len(prices) < 2:
            return 0

        max_profit = 0
        low_price = prices[0]
        for price in prices:
            if price < low_price:
                low_price = price
            elif price == low_price:
                continue
            else:
                max_profit = max(max_profit, price - low_price)

        return max_profit


def main():
    prices = [9, 8, 1, 8, 5, 4]
    s = Solution()
    max_profit = s.maxProfit(prices)
    print(max_profit)
    assert max_profit == 7

if __name__ == '__main__':
    main()
