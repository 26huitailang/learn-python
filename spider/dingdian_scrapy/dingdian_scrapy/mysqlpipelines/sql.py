#!/usr/bin/python
# coding: utf-8

import mysql.connector
from dingdian_scrapy import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:

    @classmethod  # 不需要初始化类，就可以直接调用类的方法
    def insert_dd_name(cls, xs_name, xs_author, serialstatus, serialnumber, category, name_id):
        sql = "INSERT INTO dd_name ('xs_name', 'xs_author', 'serialstatus', 'serialnumber', 'category', 'name_id') VALUES (%(xs_name)s, %(xs_author)s, %(serialstatus)s, %(serialnumber)s, %(category)s, %(name_id)s)"
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
        查找name_id这个字段，如果存在则返回1不存在返回0
        """
        sql = "SELECT EXISTS (SELCET 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

"""
DROP TABLE IF EXISTS dd_name
CREATE TABLE dd_name (
    id int(11) NOT NULL AUTO_INCREMENT,
    xs_name varchar(255) DEFAULT NULL,
    xs_author varchar(255) DEFAULT NULL,
    category varchar(255) DEFAULT NULL,
    name_id varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;
"""