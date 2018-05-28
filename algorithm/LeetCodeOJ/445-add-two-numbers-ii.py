# https://leetcode.com/problems/add-two-numbers-ii/description/
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
        result_int = self.parse_node(l1) + self.parse_node(l2)
        list_int = [int(x) for x in list(str(result_int))]
        r = self.generate_list_node(list_int)
        return r
        
    def parse_node(self, node):
        r = []
        while node:
            r.append(node.val)
            node = node.next
        r = [str(x) for x in r]
        return int("".join(r))
    
    def generate_list_node(self, val_list):
        head = ListNode(val_list[0])
        p = head
        for i in val_list[1:]:
            p.next = ListNode(i)
            p = p.next
        return head
        