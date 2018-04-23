#!/usr/bin/python
# coding: utf-8


import os
import sqlite3

DB_PATH = 'C:/Users/26hui/Desktop/mzitu'
DB_NAME = 'mzitu.db'


def get_conn(path=DB_PATH, db_name=DB_NAME):
    db_url = os.path.join(path, db_name)
    conn = sqlite3.connect(db_url)

    return conn


def create_table():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        'create table proxy_ip (id INTEGER PRIMARY KEY AUTOINCREMENT, ip varchar(16), port varchar(16), is_valid integer(1))'
    )
    cursor.close()


def get_proxy_ip_valid():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT ip, port from proxy_ip WHERE is_valid=?', (1,))
    results = cursor.fetchall()
    cursor.close()

    return results


def mark_proxy_ip_not_valid(ip, port):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('UPDATE proxy_ip SET is_valid = 0 WHERE ip=? AND port=?;', (ip, port))
    conn.commit()
    conn.close()

def insert_proxy_ip(ip, port, is_valid=1):
    text = 'INSERT INTO proxy_ip (ip, port, is_valid) VALUES(?,?,?)'
    conn = get_conn()
    with conn:
        cursor = conn.cursor()
        r = cursor.execute("SELECT * from proxy_ip WHERE ip=? and port=?", (ip, port))
        if r.fetchone():
            return False
        cursor.execute(text, (ip, port, is_valid))

        return True
