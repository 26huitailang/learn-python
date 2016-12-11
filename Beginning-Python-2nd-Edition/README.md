# Beginning-Python-2nd-Edition

- [ ] CHAPTER 1 Instant Hacking: The Basics
- [ ] CHAPTER 2 Lists and Tuples
- [ ] CHAPTER 3 Working with Strings
- [ ] CHAPTER 4 Dictionaries: When Indices Won’t Do
- [ ] CHAPTER 5 Conditionals, Loops, and Some Other Statements
- [ ] CHAPTER 6 Abstraction
- [x] CHAPTER 7 More Abstraction
- [ ] CHAPTER 8 Exceptions161
- [ ] CHAPTER 9 Magic Methods, Properties, and Iterators
- [ ] CHAPTER 10 Batteries Included
- [x] CHAPTER 11 Files and Stuff
- [ ] CHAPTER 12 Graphical User Interfaces
- [x] CHAPTER 13 Database Support
- [x] CHAPTER 14 Network Programming
- [x] CHAPTER 15 Python and the Web
- [x] CHAPTER 16 Testing, 1-2-3
- [ ] CHAPTER 17 Extending Python
- [ ] CHAPTER 18 Packaging Your Programs
- [ ] CHAPTER 19 Playful Programming
- [x] CHAPTER 20 Project 1: Instant Markup
- [x] CHAPTER 21 Project 2: Painting a Pretty Picture
- [x] CHAPTER 22 Project 3: XML for All Occasions
- [x] CHAPTER 23 Project 4: In the News
- [x] CHAPTER 24 Project 5: A Virtual Tea Party
- [x] CHAPTER 25 Project 6: Remote Editing with CGI
- [x] CHAPTER 26 Project 7: Your Own Bulletin Board
- [ ] CHAPTER 27 Project 8: File Sharing with XML-RPC
- [ ] CHAPTER 28 Project 9: File Sharing II—Now with GUI!
- [ ] CHAPTER 29 Project 10: Do-It-Yourself Arcade Game
- APPENDIX A The Short Version569
- APPENDIX B Python Reference579
- APPENDIX C Online Resources595
- APPENDIX D Python 3.0.599

---
## CH10 Batteries Included

import-only-once，在两个模块互相导入时避免发生无限循环，如果坚持要重新载入模块，可以使用內建的*reload*函数

代码重用，模块化，抽象

主程序中，__name__的值是'__main__'，而在导入的模块中，这个值被设定为模块的名字，这个设定加上if语句，可以让测试代码更好用：
```python
# hello4
def hello():
    print "hello, world!"

def test():
    hello()

if __name__ == '__main__': test()
```
作为程序运行，hello函数会被执行。而作为模块导入，不执行，就像普通模块一样：
```pythonenv
>>> import hello4
>>> hello4.hello()
hello, world!
```

*包*：模块组织好分组为包*package。包也是另一种模块，包含了许多其他模块，为了使python将一个目录作为包对待，加入__init__.py的文件（模块）。

**grok**: 神入，黑客语言，意思是完全理解、通过感觉意会，源自Robert A.Heinlein的小说*Stranger in a Strange Land*（《陌生徒弟上的陌生人》Ace Books，1995年重新发行）

### 如何探索新的模块
1. 谁用dir：查看模块包含的内容，将对象（以及模块的所有函数、类、变量等）所有特性列出。打印过滤掉模块内部的特性：
```python
[n for n in dir(copy) if not n.startswith('_')]
```
2. __all__变量，是在模块内部定义的，__all__ = ["Error", "copy", "deepcopy"]，定义了模块的公有接口，如果使用from copy import *，导入的就是__all__中的几个函数，要导入其他PyStringMap的话就要显式实现或显式调用。

3. help函数，help(copy.copy),print copy.copy.__doc__

### 标准库
- sys，让你访问与python解释器联系紧密的变量和函数
- os
    - os.sep用于路径名中的分隔符，UNIX中标准是“/”，windows中是“\\”。
    - os.system，windows下调用，os.system(r'd:\"Program Files"\xxx.exe')，空格的文件名需要单独引用
    - os.startfile，windows特有的函数，可以解决windows的路径问题，os.startfile(r'd:\Program Files\xxx.exe')
- fileinput，轻松遍历文本文件的所有行。
    ```python
    python some_script.py file1.txt file2.txt file3.txt
    ```
    > 标准输入（sys.stdin）的文本进行遍历，使在UNIX的管道中，使用标准的命令cat：
    ```unix
    cat file.txt | python some_script.py
    ```
    > 假设python每行只有40个字符，使用fileinput来遍历并添加行号
    ```python
    # numberlines.py

    import fileinput

    for line in fileinput.input(inplace=True):
        line = line.rstrip()
        num = fileinput.lineno()
        print '%-40s %2i' % (line, num)
    ```
    > 运行于程序本身
    ```run
    python numberlines.py numberlines.py
    ```

- 集合 set
- 堆 heap
- 双端队列 double-ended或deque

- time
- random 实际为伪随机。为了接近真正的随机性可以使用urandom函数，或者random模块内的SystemRandom类
---
## CH13 Database Support

- 全局变量
- 异常，except块捕捉
- 连接和游标
> 关闭了连接但还有未提交会隐式回滚，应该在每次关闭连接前进行提交
> cursor游标对象，通过cursor执行SQL查询并检查结果

_SQLite_，小型，不需要对立服务器运行，不基于集中式数据库存储机制，直接作用于本地文件。

- 代码13-1，sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 10, and there are 53 supplied.
> [:field_count] -> [: 10]

- 代码13-2， query语句的表名写错为FOOD，fiber >= 10用的数据全被排除。

---
## Project1-Instant-Markup

自己构建一个解析器来分析文章中的各种标记，并且输出为HTML形式。类似Markdown。

---
## Project2-Painting-a-Pretty-Picture

利用urllib网上抓取txt的数据并过滤，使用reportlab包完成绘图并输出为pdf。

看过pandas，觉得pandas实现更简单，特别是数据处理方面。

---
## Project3-XML-for-All-Ocassions
用XML构建一个网站，自己解析并生成html文件。

---
## Project4-In-the-News
[free usenet server](http://www.freeusenetnews.com/)
server: news2.neva.ru

---
## Project5-A-Virtual-Tea-Party
主要功能：
- 服务器能接受来自不同用户的多个连接
- 允许用户同时（并行）操作
- 能够解释命令，例如，say后者logout
- 容易扩展

---
## Project6-Remote-Editing-with-CGI

**CGI:** 将网页表单内容提供给可编程语言进行处理。

主要功能：
- 将文档作为普通网页显示
- 在Web表单的文本域内显示文档
- 保存表单中的文本
- 使用密码保护文档
- 容易扩展，以支持处理多于一个文档的情况

**使用CGI的POST方法替代默认的GET，提交大量数据时一般使用POST**

### 问题

- 代码从windows平台拷贝到linux环境中运行时，否则无法运行。
> 注意转换line endings，CRLF(WIN)->LF(类Unix)。

---
## Project7-Your Own Bulletin Board
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

### 问题：

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
```

---
## Project8-File Sharing with XML-RPC

前置章节：
- 10 batteries included
- 14 socket
- 15 网络
- 24 socket

**P2P**：任何节点peer都可以连接到其他节点，在这样一个由节点组成的网络中，是没有中央节点的（C/S架构中的服务器所表现的），这样网络会更**强壮**。除非大多数节点关闭了，否则网络是不会崩溃的。

finished.

### tips
- startswith错写为startwith
