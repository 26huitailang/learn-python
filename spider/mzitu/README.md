down_mzitu.py这个程序是用于爬取妹子图网站图片的爬虫代码，主要环境是：
- 运行环境：虚拟的python3.6.0
- 需要额外安装的package：
    - BeautifulSoup，实现爬虫的主要功能
    - pymongo，对接MongoDB
    - requests，urllib的升级集合使用简单
    - datetime，简单使用的time模块
- 数据库：MongoDB

- down_mzitu.py

是可以去重的单进程爬虫，可以自动更换User-Agent和ip proxy。

- download.py

更换UA和ip proxy发起请求的代码，单进程或多进程的request都是调用的这个文件。

- get_all_pages.py

获取总页面上的所有套图地址文档，并写入到meinvxiezhenji数据库的crawl_queue集合中。

- mongodb_queue.py

构建队列的代码，里面有一个队列对象以及各种操作的方法。

- mzitu.py

一个最基础的爬取图片的网站，不稳定，每次挂掉需要重新下载。

# 运行
````
python mzitu.py  # 最简单的
or
python down_mzitu.py  # 用数据库记录去重的
or
\\TODO 多进程的运行方式
```


