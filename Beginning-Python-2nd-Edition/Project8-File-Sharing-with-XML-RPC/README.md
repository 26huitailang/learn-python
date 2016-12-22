# Project8-File Sharing with XML-RPC

前置章节：
- 10 batteries included
- 14 socket
- 15 网络
- 24 socket

**P2P**：任何节点peer都可以连接到其他节点，在这样一个由节点组成的网络中，是没有中央节点的（C/S架构中的服务器所表现的），这样网络会更**强壮**。除非大多数节点关闭了，否则网络是不会崩溃的。

**finished.**

### tips
- startswith错写为startwith
=======
验证文件名：使用os.path模块，可以实现不依赖平台（Windows、UNIX和Mac OS都行）的方案，方法是创建由目录名和文件名组成的绝对路径，目录名和空文件名连接起来（使用os.path.join）保证结尾是文件分隔符（比如'/'），然后就可以检查绝对文件名是否以绝对目录名开始。如果是的话，那么文件就存在目录中。