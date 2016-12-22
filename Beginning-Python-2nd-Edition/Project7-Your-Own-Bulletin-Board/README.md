# Project7-Your Own Bulletin Board
前置：CH13数据库内容
PostgreSQL -> sudo apt-get install python-psycopg2

引用：

```python
from psycopg2 import psycopg1 as psycopg
```

Linux 测试：
```python
from psycopg2 import psycopg1 as psycopg
conn = psycopg.connect('user=bar dbname=bar password=123456')
curs = conn.cursor()
curs.execute('SELECT * FROM messages')
curs.fetchall()
```

字段列表：
- id: 用于标识唯一的消息
- subject: 包括消息主题的字符串
- sender: 包括发送者名字、Email地址的或其他信息的字符串
- reply_to: 如果消息是回复其他信息的，那么这个字段就包括那个消息的id（否则，字段就是空的）
- text: 包括消息内容的字符串

## 问题：

PostgreSQL
- psycopg2.ProgrammingError: permission denied for relation messages

> GRANT on the database is not what you need. Grant on the tables directly.
>Granting privileges on the database mostly is used to grant or revoke connect privileges. This allows you to specify who may do stuff in the database if they have sufficient other permissions.
```SQL
GRANT ALL PRIVILEGES ON TABLE table_name TO user;
```

- 单引号'转义（逃逸）

> 使用两个单引号即可，教程中的“\\'"有误

- permission denied for sequence messages_id_seq

> Since PostgreSQL 8.2 you have to use:
```SQL
GRANT USAGE, SELECT ON SEQUENCE messages_id_seq TO bar;
```
> GRANT USAGE - For sequences, this privilege allows the use of the currval and nextval functions.

- FATAL: Peer authentication failed for user “bar”

> 1.运行下面的命令编辑pg_hba.conf文件
```Linux
sudo gedit /etc/postgresql/9.1/main/pg_hba.conf
```
> 2.将

> \# Database administrative login by Unix domain socket

> local   all    postgres     peer

> 改为

> \# Database administrative login by Unix domain socket

> local   all       postgres    trust或md5

> 3.保存后执行下面的命令重新加载配置文件:
```Linux
sudo /etc/init.d/postgresql reload
```

- PostgreSQL -> sudo apt-get install python-psycopg2，在笔记本上报错python2.7-minimal

> 在提示出错后，修改 /usr/share/python/runtime.d/public_modules.rtinstall，注释掉所有的内容，（注释sh方法 : 'BLOCK  代码块  BLOCK'，BLOCK可省），然后
```Linux
apt-get -f install 
```
> 待正常后，再执行一次
```Linux
pycompile -V 2.7 /usr/lib/python2.7/dist-packages