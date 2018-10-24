# coding: utf-8
"""
标记出每个kgroup，然后用标准的反转链表做法。
注意点：
  - 反转后的kgroup怎么链接起来，用一个指针记录每次翻转后group的最后位置，然后链接到下一个kgroup的第一个元素
  - 翻转的时候，第一次会把第一个元素指向下一个group的第一个元素，这样最后一个group小于k的话，也是正确的链表格式

答案是discuss里面的不错的，可以试着用pudb观察标记的变化
"""
import pudb; pudb.set_trace()
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # 移动r到group的边界
                r = r.next
                count += 1
            if count == k:  # 说明满足k条件，需要翻转
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l =  pre, l, r  # 链接两个group
            else:
                return dummy.next  # dummy.next 总是指向第一个元素


def main():
    node_list = [ListNode(n) for n in range(10)]
    head = node_list[0]
    temp = head
    for node in node_list[1:]:
        temp.next = node
        temp = temp.next
    sl = Solution()
    result = sl.reverseKGroup(head, 3)
    while result:
        print(result.val)
        result = result.next

if __name__ == '__main__':
    main()