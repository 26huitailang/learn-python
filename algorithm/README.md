先在github的reademe完成，定期更新到blog上。
------------------------------
# LeetCode
链接是leetcode地址：

- [1. Two Sum](https://leetcode.com/problems/two-sum/description/) 字典
- [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/description/) ascii码，26进制
- [617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/description/) 递归

# 算法与数据结构
[八大排序](http://python.jobbole.com/82270/)，`/sort/basicSort.py`：
- [x] [冒泡bubble]，冒泡排序因为是在原数组上直接操作，所以它占的空间资源较少，在数据量不大的情况还是挺好的。但是由于算法涉及双重循环，所以在数据量大的情况下，程序运行的时间是相当长的，因为要一次一次地遍历数据。
- [x] 插入排序，插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
- [ ] 希尔排序
- [ ] 快速排序
- [ ] 直接选择排序
- [ ] 堆排序
- [ ] 基数排序
- [x] Hash，见`/Hash`目录。

## 稳定排序和不稳定排序

[参考](http://www.cnblogs.com/codingmylife/archive/2012/10/21/2732980.html)

简单说就是，如果有两个相同的数，在排序前后相对位置关系不变。

- 稳定排序：冒泡，插入，归并，基数排序
- 不稳定排序：选择，快速，希尔，堆排序







