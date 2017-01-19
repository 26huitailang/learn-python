#!/usr/bin/python
# coding: utf-8
import six
import sys


class HuffNode(object):
    """
    定义一个HuffNode虚类，里面包含两个虚方法
    1. 获取节点的权重函数
    2. 获取此节点是否是叶节点的函数
    """
    def get_weight(self):
        raise NotImplementedError("The Abstract Node Close doesn't define 'get_weight'")

    def isleaf(self):
        raise NotImplementedError("The Abstract Node Close doesn't define 'isleaf'")


class LeafNode(HuffNode):
    """
    树叶节点类
    """
    def __init__(self, value=0, freq=0):
        """
        初始化树节点，需要初始化的对象参数有：value及出现的频率freq
        """
        super(LeafNode, self).__init__()
        # 叶子节点的字符
        self.value = value
        # 字符出现的频率，也就是叶节点的权重
        self.weight = freq

    def isleaf(self):
        """
        基类的方法，返回True，代表是叶节点
        """
        return True

    def get_weight(self):
        """
        基类的方法，返回对象属性weight，表示对象的权重
        """
        return self.weight

    def get_value(self):
        """
        获取叶子节点的字符的值
        """
        return self.value


class IntlNode(HuffNode):
    """
    中间节点类
    """
    def __init__(self, left_child=None, right_child=None):
        """
        初始化中间节点需要初始化的对象参数有：left_child, right_child, weight
        """
        # ??
        super(IntlNode, self).__init__()
        # 节点的值
        self.weight = left_child.get_weight() + right_child.get_weight()
        # 左右子节点
        self.left_child = left_child
        self.right_child = right_child

    def isleaf(self):
        """
        基类的方法，返回False，代表是中间节点
        """
        return False

    def get_weight(self):
        """
        基类的方法，返回对象属性weight，表示对象的权重
        """
        return self.weight

    def get_left(self):
        """
        获取左子节点
        """
        return self.left_child

    def get_right(self):
        """
        获取右子节点
        """
        return self.right_child


class HuffTree(object):
    """
    HuffTree
    """
    def __init__(self, flag, value=0, freq=0, left_tree=None, right_tree=None):
        super(HuffTree, self).__init__()
        if flag == 0:
            self.root = LeafNode(value, freq)
        else:
            self.root = IntlNode(left_tree.get_root(), right_tree.get_root())

    def get_root(self):
        """
        获取huffman tree的根节点
        """
        return self.root

    def get_weight(self):
        """
        获取这个huffman树的根节点的权重
        """
        return self.root.get_weight()

    def traverse_huffman_tree(self, root, code, char_freq):
        """
        利用递归的方法遍历huffman树，并且以此方式得到每个字符对应的huffman编码，保存在字典char_freq中
        """
        if root.isleaf():
            char_freq[root.get_value()] = code
            print("it = %d/%c and freq = %d code = %s") % (root.get_value(), chr(root.get_value()), root.get_weight(), code)
            return None
        else:
            self.traverse_huffman_tree(root.get_left(), code + '0', char_freq)
            self.traverse_huffman_tree(root.get_right(), code + '1', char_freq)


def buildHuffmanTree(list_hufftrees):
    """
    构造huffman树的方法
    """
    while len(list_hufftrees) > 1:
        # 1. 按照weight对huffman树进行从小到大的排序
        list_hufftrees.sort(key=lambda x: x.get_weight())
        # 2. 挑出weight最小的两个组成huffman编码树
        temp1 = list_hufftrees[0]
        temp2 = list_hufftrees[1]
        list_hufftrees = list_hufftrees[2:]

        # 3. 构造一个新的huffman树
        newed_hufftree = HuffTree(1, 0, 0, temp1, temp2)

        # 4. 放入到数组当中
        list_hufftrees.append(newed_hufftree)

    # last. 数组中最后剩下来的那棵树，就是构造的huffman编码树
    return list_hufftrees[0]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Please input inputfile name"
        exit(0)
    else:
        INPUTFILE = sys.argv[1]

    f = open(INPUTFILE, 'rb')
    filedata = f.read()
    filesize = f.tell()

    char_freq = {}
    for x in range(filesize):
        tem = six.byte2int(filedata[x])
        if tem in char_freq.keys():
            char_freq[tem] = char_freq[tem] + 1
        else:
            char_freq[tem] = 1

    for tem in char_freq.keys():
        print tem, ':', char_freq[tem]

    list_hufftrees = []
    for x in char_freq.keys():
        tem = HuffTree(0, x, char_freq[x], None, None)
        list_hufftrees.append(tem)

    tem = buildHuffmanTree(list_hufftrees)
    tem.traverse_huffman_tree(tem.get_root(), '', char_freq)
