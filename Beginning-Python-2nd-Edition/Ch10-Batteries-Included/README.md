# CH10 Batteries Included

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

## 如何探索新的模块
1. 谁用dir：查看模块包含的内容，将对象（以及模块的所有函数、类、变量等）所有特性列出。打印过滤掉模块内部的特性：
```python
[n for n in dir(copy) if not n.startswith('_')]
```
2. __all__变量，是在模块内部定义的，__all__ = ["Error", "copy", "deepcopy"]，定义了模块的公有接口，如果使用from copy import *，导入的就是__all__中的几个函数，要导入其他PyStringMap的话就要显式实现或显式调用。

3. help函数，help(copy.copy),print copy.copy.__doc__

## 标准库
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

