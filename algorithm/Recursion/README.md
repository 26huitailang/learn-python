# 递归

## 参考

- [极客时间](https://time.geekbang.org/column/article/41440)

## 认识

递归是一种应用非常广泛的编程技巧，很多数据结构和算法都要用到递归，比如DFS深度优先搜索、前中后序二叉树遍历等等。

递归的分解：

- 一个问题可以分解为多个子问题，子问题除了数据规模不同，求解思路是一致的
- 搞明白基线条件（终止条件），不然可能存在无限循环或溢出的情况

在思考递归问题的时候，切忌尝试自己用脑子去展开整个递归的过程，很容易被绕晕，感觉这也是初学递归最容易犯的错误。尝试只思考一个问题和它子问题的关系即可，以及最后的终止条件。

编码：

- 基线条件
- 递归条件

注意：

- 小心堆栈溢出，比如python一般在1000左右深度的时候就会溢出，报错`RecursionError`。
- 警惕重复的计算，比如爬阶梯的问题，f(k)可能会在递归过程中对此被计算，为了避免重复计算，可提供一个数据结构（比如散列表）来保存已经求过的f(k)，调用前先查看是否有结果。
- 递归在时间和空间复杂度分析上，考虑函数的多次调用

## 递归改写为非递归

几乎所欲的递归都能改写为非递归的形式。

避免栈溢出还可以了解`尾递归`的概念。