# coding: utf-8
"""wiki链接六度分离问题，用广度优先搜索算法
数据来自wiki_mysql_count6.py对于wiki Kevin_Bacon词条的采集，持久化于mysql wikipedia中，有links和pages两张表，分别存储到达关系和wiki页面链接
"""
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')


class SolutionFound(RuntimeError):
    """
    解决方案发现类，发送相应的信号
    """
    def __init__(self, message):
        self.message = message


def getLinks(fromPageId):
    """
    得到fromPageId为起始的所有toPageId
    :param fromPageId: links表中的起始页面，在pages表中对应链接id
    :return: 返回fromPageId对应的所有toPageId
    """
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    # 搜索结果为空返回None
    if cur.rowcount == 0:
        return None
    # 否则以list形式返回所有的
    else:
        return [x[0] for x in cur.fetchall()]


def constructDict(currentPageId):
    """
    根据currentPageId构建字典
    :param currentPageId: 当前PageId，作为fromPageId传入getLinks
    :return: 如果有toPageId，则返回根据list构建的字典，否则返回空字典
    """
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}


# 链接树要么为空，要么包含多个链接
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    # 有初始值，为0停止递归，返回链接树
    if depth == 0:
        return linkTree
    # 如果链接树为空（初始为{})，根据currentPageId构建
    if not linkTree:
        linkTree = constructDict(currentPageId)
        # 构建结果为空，表示currentPageId没有toPageId
        if not linkTree:
            # 若此节点页面无连接，则跳过此节点
            return {}
    # 如果目标id在链接树中，打印结果，并抛出SolutionFound
    if targetPageId in linkTree.keys():
        print("TARGET " + str(targetPageId) + " FOUND!")
        raise SolutionFound("PAGE: " + str(currentPageId))

    # {brachKey: {} ...}遍历
    for branchKey, branchValue in linkTree.items():
        try:
            # 递归建立链接树，相当于下一层，所以depth-1
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth - 1)
        # 捕捉SolutionFound
        except SolutionFound as e:
            print(e.message)
            # 抛出当前的pageId
            raise SolutionFound("PAGE: " + str(currentPageId))
    # 如果都没有，则返回linkTree，完成这一层的递归
    return linkTree

# 总是以捕捉SolutionFound，来执行最后消息的打印，否则没有解决方案
try:
    searchDepth(3850, 1, {}, 4)
    # 链接节点为空
    print("No solution found")
except SolutionFound as e:
    print(e.message)