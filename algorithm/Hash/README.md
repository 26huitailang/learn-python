大部分内容来自这篇[博客](http://www.cnblogs.com/dolphin0520/archive/2012/09/28/2700000.html)。
# Hash表
哈希表也称散列表，一种特殊的数据结构，不同于数组、链表、二叉树等，它能快速定位查找记录，并不是通过与表中存在的记录进行关键字比较查找。python中的字典便是用hash表实现的。

优点很明显就是速度快，时间复杂度总是在常数级，插入和删除数据比较容易。

缺点是不支持排序，比一般线性表占用更多的空间，并且关键字不能重复。

所以，哈希表或者说python中的dict是一种用空间换取时间的做法。

# 关键知识点

## Hash函数设计

1. 直接定址法
2. 平方取中法
3. 折叠法
4. 取余法

## 表大小的确定

过大会造成空间浪费，取小了会造成冲突，限制查找速度。
- 可以根据实际记录存储个数和关键字分布特点确定
- 在未知的情况下也可以动态维护Hash表的大小

## 冲突的解决
通常情况以下两种：
1. 开放定址法：当产生冲突时，用某种探测规则（如线性探测）依次查找，直到遇到空单元。
2. 链地址法：数组和链表相结合的方法，将hash地址相同的记录存储到一个线性表中，表头为计算所得的hash地址。

## 平均查找速度
Hash表的平均查找长度包括查找成功时的平均查找长度和查找失败时的平均查找长度。

- 查找成功时的平均查找长度=表中每个元素查找成功时的比较次数之和/表中元素个数；

- 查找不成功时的平均查找长度相当于在表中查找元素不成功时的平均比较次数，可以理解为向表中插入某个元素，该元素在每个位置都有可能，然后计算出在每个位置能够插入时需要比较的次数，再除以表长即为查找不成功时的平均查找长度。

- __装填因子__=表中的记录数/哈希表长度，越小表明表中空单元越多，越大则越易引起冲突，影响查找的效率。一般情况下，装填因子在0.5时比较合适。

# python中字典实现

找资料时发现的有人[翻译的文档](https://harveyqing.gitbooks.io/python-read-and-write/content/python_advance/python_dict_implementation.html)，这里大家可以参考下。