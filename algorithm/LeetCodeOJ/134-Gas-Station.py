class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        """来自讨论的方案"""
        refuel = list(map(lambda x, y: x - y, (gas, cost))
        if sum(refuel) < 0:
            return -1
        start, total, min_val = 0, 0, 0
        for i range(len(gas)):
            total += gas[i] - cost[i]
            if total < min_val :
                start = i + 1  # 最小值的下一站就是出发点
                min_val  = total
                
        return start 

