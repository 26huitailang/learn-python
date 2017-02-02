#!/usr/bin/python
# coding: utf-8

import mysql.connector
from dingdian_scrapy import settings

# 从settings文件导入配置
MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

# 创建数据库的连接
cnx = mysql.connector.connect(user=MYSQL_USER,
                              password=MYSQL_PASSWORD,
                              host=MYSQL_HOSTS,
                              database=MYSQL_DB)
# 初始化游标
cur = cnx.cursor(buffered=True)


class Sql:
    """
    Sql类，用于定义操作数据库的方法，插入和去重
    insert_dd_name
    select_name
    insert_dd_chaptername
    select_chapter
    """
    @classmethod  # 不需要初始化类，就可以直接调用类的方法
    def insert_dd_name(cls, xs_name, xs_author, serialstatus, serialnumber, category, name_id):
        """
        将小说的相关信息插入数据库
        :param xs_name:小说名字
        :param xs_author:小说作者
        :param serialstatus:连载状态
        :param serialnumber:连载字数
        :param category:分类
        :param name_id:小说编号
        :return:None
        """
        sql = "INSERT INTO dd_name (xs_name, xs_author, serialstatus, serialnumber, category, name_id) VALUES (%(xs_name)s, %(xs_author)s, %(serialstatus)s, %(serialnumber)s, %(category)s, %(name_id)s)"
        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'serialstatus': serialstatus,
            'serialnumber': serialnumber,
            'category': category,
            'name_id': name_id
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_name(cls, name_id):
        """
        查找name_id这个字段，EXISTS会返回满足条件的Boolean
        :param name_id:小说编号
        :return:如果存在则返回1不存在返回0，如果子查询不止一个，则返回一列1或0
        """
        sql = "SELECT EXISTS (SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        # 返回结果的第一位
        return cur.fetchall()[0]

    @classmethod
    def insert_dd_chaptername(cls, xs_chaptername, xs_content, id_name, num_id, url):
        """
        将章节内容及相关信息插入数据库
        :param xs_chaptername:章节名称
        :param xs_content:章节内容
        :param id_name:小说编号
        :param num_id:在异步中保持章节的顺序，计数器
        :param url:章节地址
        :return:None
        """
        sql = "INSERT INTO dd_chaptername (xs_chaptername, xs_content, id_name, num_id, url) VALUES (%(xs_chaptername)s, %(xs_content)s, %(id_name)s, %(num_id)s, %(url)s)"
        value = {
            'xs_chaptername': xs_chaptername,
            'xs_content': xs_content,
            'id_name': id_name,
            'num_id': num_id,
            'url': url
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_chapter(cls, url):
        """
        查询章节是否重复
        :param url:章节地址
        """
        sql = "SELECT EXISTS (SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
        value = {'url': url}
        cur.execute(sql, value)
        return cur.fetchall()[0]


"""用于创建数据库的SQL
DROP TABLE IF EXISTS dd_name
CREATE TABLE dd_name (
    id int(11) NOT NULL AUTO_INCREMENT,
    xs_name varchar(255) DEFAULT NULL,
    xs_author varchar(255) DEFAULT NULL,
    serialstatus varchar(255) DEFAULT NULL,
    serialnumber varchar(255) DEFAULT NULL,
    category varchar(255) DEFAULT NULL,
    name_id varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS dd_chaptername;
CREATE TABLE dd_chaptername (
  id int(11) NOT NULL AUTO_INCREMENT,
  xs_chaptername varchar(255) DEFAULT NULL,
  xs_content text,
  id_name int(11) DEFAULT NULL,
  num_id int(11) DEFAULT NULL,
  url varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2726 DEFAULT CHARSET=gb18030;
SET FOREIGN_KEY_CHECKS=1;
"""
