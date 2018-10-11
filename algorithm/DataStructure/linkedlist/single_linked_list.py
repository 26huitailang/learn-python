# coding: utf-8

import types


def tramp(gen, *args, **kwargs):
    # 执行generator到最后的结果
    # 这里是用来实现尾递归的效果
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)  # python3 version, python2 is g.next()
    return g


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "{}".format(self.value)


class SingleLinkedList(object):
    """单链表"""

    def __init__(self, head=None):
        self.head = head

    def initialize(self, node_list):
        # 根据节点列表初始化一个链表
        if not node_list:
            return
        self.head = node_list[0]
        temp = self.head
        for node in node_list[1:]:
            temp.next = node
            temp = temp.next
        return self.head

    def is_empty(self):
        # 判断链表为空
        if self.head is None:
            return True
        else:
            return False

    def get_length(self):
        count = 0
        if self.head is None:
            return count

        p = self.head
        while p:
            p = p.next
            count += 1

        return count

    def push(self, node):
        # 尾部插入
        if self.is_empty():
            self.head = node
            return True

        p = self.head
        while p.next:
            p = p.next
        p.next = node
        return True

    def traverse(self):
        # 遍历
        if self.is_empty():
            print("Link list is empty")
            return

        print('traverse result:')
        node = self.head
        result = list()
        while node:
            result.append(node.value)
            node = node.next
        print('->'.join([str(x) for x in result]))

    def reverse_by_recursion(self, node):
        # 反转，1->2->3->None，3->2->1->None
        # node起始传入head
        # 链表太长会超过递归的系统默认限制，1000，通过sys.setrecursionlimit(10000)可以解决，不过不推荐

        # 基线条件
        if node.next is None:
            self.head = node
        # 递归条件
        else:
            self.reverse_by_recursion(node.next)
            node.next.next = node  # 下一节点的引用指向该节点
            node.next = None  # 该节点的引用设为None

        return self.head

    # python 不真正的支持尾递归
    # 装饰器实现参考 http://python.jobbole.com/86937/
    # 也可以利用python的generate特性
    def _tail_recursion(self, first, second):
        tmp = second.next
        second.next = first
        if tmp is None:
            self.head = second
            yield self.head

        yield self._tail_recursion(second, tmp)

    def reverse_by_tail_recursion(self):
        result = tramp(self._tail_recursion, None, self.head)
        return result

    def reverse_by_loop(self):
        # 思路将下一个节点以头部插入的方式来修改引用
        if self.head is None or self.head.next is None:
            return

        pre = None
        cur = self.head
        while cur:
            self.head = cur  # 当前节点修改为头节点
            tmp = cur.next  # 保存下一个节点的引用
            cur.next = pre  # 修改为前一个节点的引用
            pre = cur  # 记录为前一个节点
            cur = tmp  # cur修改为下一个节点
        return self.head

    def entry_node_of_loop(self):
        # 链表中环的入口节点，如果存在就表明有环，否则，无
        # 思路1: 用一个容器放入已查看节点或者先遍历所有，如果访问遇到容器中有重复，则是
        # 思路2: 快慢指针相遇
        # 以下是思路1的实现
        if self.head is None:
            return
        visited_nodes = []
        visited_nodes.append(self.head)
        p = self.head.next
        while p:
            if p in visited_nodes:
                return p
            visited_nodes.append(p)
            p = p.next
        return

    def del_nth_from_end(self, n):
        # 删除倒数第n个节点，最简单的时获得长度计算正数的第几个
        # 遍历一遍的思路，两个指针，第一个先走n步到达尾部的时候，第二个指针指向要删除的节点
        p = self.head
        q = self.head
        for _ in range(n):
            p = p.next
        while p.next:
            p = p.next
            q = q.next  # 不要越过要删除的点
        tmp = q.next.next
        q.next.next = None  # 将要删除节点的引用置为None
        q.next = tmp  # q.next 指向要删除的节点，修改为下下一个节点即可

        return self.head

    def find_middle_node(self) -> Node:
        # 思路，快慢指针，每次快指针走两步，满指针一步
        fast, slow = self.head, self.head
        fast = self.head.next if fast else None
        while fast and fast.next:  # 有可能两步后，fast已经到尾部为None
            print("slow: {} fast: {}".format(slow.value, fast.value))
            slow, fast = slow.next, fast.next.next
        return slow

def merge_two_sorted_linked_list(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    p = None
    if head1.value < head2.value:
        p = head1
        p.next = merge_two_sorted_linked_list(head1.next, head2)
    else:
        p = head2  # 相等的情况也在这里
        p.next = merge_two_sorted_linked_list(head1, head2.next)
    return p


def test():
    count = 21  # 如果要测试递归溢出，可以设置为1000及以上
    single_linked_list = SingleLinkedList()
    single_linked_list.traverse()

    print("initialize ...")
    node_list = [Node(x) for x in range(count)]
    single_linked_list.initialize(node_list)
    single_linked_list.traverse()
    assert single_linked_list.get_length() == count
    middle_node = single_linked_list.find_middle_node()
    print("middle_node {}".format(middle_node.value))
    print('=' * 20)

    print("push ...")
    single_linked_list.push(Node(count))
    single_linked_list.traverse()
    print('=' * 20)

    nth = count // 3
    print("delete nth={} node from end ...".format(nth))
    single_linked_list.del_nth_from_end(nth)
    single_linked_list.traverse()
    print('=' * 20)

    print("reverse by recursion ...")
    try:
        single_linked_list.reverse_by_recursion(single_linked_list.head)
        single_linked_list.traverse()
    except RecursionError as e:
        print(e)
    print("reverse by tail recursion ...")
    single_linked_list.reverse_by_tail_recursion()
    single_linked_list.traverse()
    print("reverse by loop ...")
    single_linked_list.reverse_by_loop()
    single_linked_list.traverse()
    print('=' * 20)

    print("entry_node_of_loop ...")
    entry = single_linked_list.entry_node_of_loop()
    print(entry)
    print("created a link list loop ...")
    last_node = single_linked_list.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = single_linked_list.head
    entry = single_linked_list.entry_node_of_loop()
    print(entry)
    print('=' * 20)

    print("merger two sorted linked list ...")
    node_list1 = [Node(x) for x in range(0, count, 2)]
    node_list2 = [Node(x) for x in range(1, count, 2)]
    sl1 = SingleLinkedList()
    sl2 = SingleLinkedList()
    sl1.initialize(node_list1)
    sl2.initialize(node_list2)
    sl1.traverse()
    sl2.traverse()
    try:
        merged_linked_list = merge_two_sorted_linked_list(sl1.head, sl2.head)
        merged_linked_list = SingleLinkedList(merged_linked_list)
        merged_linked_list.traverse()
    except RecursionError as e:
        print(e)
    print('=' * 20)


if __name__ == '__main__':
    test()
