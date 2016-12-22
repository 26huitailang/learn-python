# CH13 Database Support

- 全局变量
- 异常，except块捕捉
- 连接和游标
> 关闭了连接但还有未提交会隐式回滚，应该在每次关闭连接前进行提交
> cursor游标对象，通过cursor执行SQL查询并检查结果

_SQLite_，小型，不需要对立服务器运行，不基于集中式数据库存储机制，直接作用于本地文件。

- 代码13-1，sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 10, and there are 53 supplied.
> [:field_count] -> [: 10]

- 代码13-2， query语句的表名写错为FOOD，fiber >= 10用的数据全被排除。