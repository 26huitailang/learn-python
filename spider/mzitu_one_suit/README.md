# 简介
这个小样是按照自己的想法重新写的一个小爬虫，目的是简单练习一些相关的技能，所以暂时是通过`python -m main.py http://www.mzitu.com/xxxxx`下载一个套图，喜欢的图才下，也不给这个良心站增加压力。

- 正则 re
- 队列 redis
- sql sqlite
- 多线程 threading
- 网络请求 requests

# 大概流程

- 请求一个提供免费代理的网站，将拿到的内容存入sqlite，方便后面使用来作代理
- 开始分析从命令行传入的套图首页，拿到最大页数
- 循环获取套图地址，这里用了代理，如果代理失效会将is_valid标志为false
- 将拿到的地址存入redis队列里面，格式是`{'filename': abs_filepath: 'url' : img_url, 'header_url': header_url}，这里存入reids用了json.dumps，可以保证在取出时用json.loads得到的依然是字典，header_url是请求时头部的Reference，避免反爬虫。
- 下载时取出一个下载并保存，保存路径直接拿filename就好，是绝对路径