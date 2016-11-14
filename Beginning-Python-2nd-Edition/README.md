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
- [ ] CHAPTER 26 Project 7: Your Own Bulletin Board
- [ ] CHAPTER 27 Project 8: File Sharing with XML-RPC
- [ ] CHAPTER 28 Project 9: File Sharing II—Now with GUI!
- [ ] CHAPTER 29 Project 10: Do-It-Yourself Arcade Game

- APPENDIX A The Short Version569
- APPENDIX B Python Reference579
- APPENDIX C Online Resources595
- APPENDIX D Python 3.0.599

## CH13 Database Support
全局变量

异常，except块捕捉

连接和游标
- 关闭了连接但还有未提交会隐式回滚，应该在每次关闭连接前进行提交
- cursor游标对象，通过cursor执行SQL查询并检查结果

SQLite，小型，不需要对立服务器运行，不基于集中式数据库存储机制，直接作用于本地文件。

13-1
- sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 10, and there are 53 supplied.

[:field_count] -> [: 10]

13-2
- query语句的表名写错为FOOD，fiber >= 10用的数据全被排除。

## Project1-Instant-Markup
自己构建一个解析器来分析文章中的各种标记，并且输出为HTML形式。类似Markdown。

## Project2-Painting-a-Pretty-Picture
利用urllib网上抓取txt的数据并过滤，使用reportlab包完成绘图并输出为pdf。

看过pandas，觉得pandas实现更简单，特别是数据处理方面。

## Project3-XML-for-All-Ocassions
用XML构建一个网站，自己解析并生成html文件。

## Project4-In-the-News
[free usenet server](http://www.freeusenetnews.com/)
server: news2.neva.ru

## Project5-A-Virtual-Tea-Party
主要功能：
- 服务器能接受来自不同用户的多个连接
- 允许用户同时（并行）操作
- 能够解释命令，例如，say后者logout
- 容易扩展

## Project6-Remote-Editing-with-CGI
主要功能：
- 将文档作为普通网页显示
- 在Web表单的文本域内显示文档
- 保存表单中的文本
- 使用密码保护文档
- 容易扩展，以支持处理多于一个文档的情况

**使用CGI的POST方法替代默认的GET，提交大量数据时一般使用POST**

**Tips**:代码从windows平台拷贝到linux环境中运行时，注意转换line endings，CRLF(WIN)->LF(类Unix)，否则无法运行。

## Project7-Your Own Bulletin Board
相关：CH13数据库内容
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

PostgreSQL
> psycopg2.ProgrammingError: permission denied for relation messages

    GRANT on the database is not what you need. Grant on the tables directly.
    Granting privileges on the database mostly is used to grant or revoke connect privileges. This allows you to specify who may do stuff in the database if they have sufficient other permissions.
    You want instead:
    ```SQL
    GRANT ALL PRIVILEGES ON TABLE side_adzone TO jerry;
    ```
    This will take care of this issue.
