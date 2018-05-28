# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_int = self.parse_num(l1) + self.parse_num(l2)
        result = [int(x) for x in list(str(result_int))]
        print(result)
        l = []
        while result:
            value = result.pop()
            tmp = ListNode(value)
            l.append(tmp)
        
        for i in range(len(l)):
            if i == len(l) - 1:
                  break
            l[i].next = l[i + 1]
        print(l[0])
        return l[0]
    
    def parse_num(self, node):
        tmp = []
        while True:
            tmp.append(node.val)
            node = node.next
            if node is None:
                break
        
        print(tmp)
                
        r = 0
        for i in range(len(tmp)):
            r += tmp[i] * (10 ** i)
            print(r)
        print(r)
        return r
        