# coding: utf-8


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SingleLinkedList:
    """单链表"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        # 判断链表为空
        if self.head is None:
            return True
        else:
            return False

    def traverse(self):
        # 遍历
        if self.is_empty():
            print("Link list is empty")
            return
        
        print('traverse result:')
        node = self.head
        while node:
            print(node.value)
            node = node.next

single_linked_list = SingleLinkedList()
single_linked_list.traverse()
node_list = [Node(x) for x in range(10)]
single_linked_list.head = node_list[0]
temp = single_linked_list.head
for node in node_list[1:]:
    temp.next = node
    temp = temp.next
single_linked_list.traverse()
