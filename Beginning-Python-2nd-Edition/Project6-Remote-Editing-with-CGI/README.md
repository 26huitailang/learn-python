# Project6-Remote-Editing-with-CGI

**CGI:** 将网页表单内容提供给可编程语言进行处理。

主要功能：
- 将文档作为普通网页显示
- 在Web表单的文本域内显示文档
- 保存表单中的文本
- 使用密码保护文档
- 容易扩展，以支持处理多于一个文档的情况

**使用CGI的POST方法替代默认的GET，提交大量数据时一般使用POST**

## 问题

- 代码从windows平台拷贝到linux环境中运行时，否则无法运行。
> 注意转换line endings，CRLF(WIN)->LF(类Unix)。