# update, ex36 a pyramid game, try to make a to-do list first.
#coding:utf-8
#author:Elvis
 
class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.l_child = None
        self.r_child = None
 
class Tree(TreeNode):
    #create a tree
    def create_tree(self, tree):
        data = raw_input('->')
        if data == '#':
            tree = None
        else:
            tree.data = data
            tree.l_child = TreeNode()
            self.create_tree(tree.l_child)
            tree.r_child = TreeNode()
            self.create_tree(tree.r_child)
 
    #visit a tree node
    def visit(self, tree):
        #输入#号代表空树
        if tree.data is not '#':
            print str(tree.data) + '\t',
    #先序遍历
    def pre_order(self, tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.l_child)
            self.pre_order(tree.r_child)
 
    #中序遍历
    def in_order(self, tree):
        if tree is not None:
            self.in_order(tree.l_child)
            self.visit(tree)
            self.in_order(tree.r_child)
 
    #后序遍历
    def post_order(self, tree):
        if tree is not None:
            self.post_order(tree.l_child)
            self.post_order(tree.r_child)
            self.visit(tree)
 
t = TreeNode()
tree = Tree()
tree.create_tree(t)
tree.pre_order(t)
print '\n'
tree.in_order(t)
print '\n'
tree.post_order(t)