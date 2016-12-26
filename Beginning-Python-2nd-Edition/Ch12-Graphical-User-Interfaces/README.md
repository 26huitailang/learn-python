CH12 Graphical User Interfaces(GUI)

一些流行的GUI工具包：

- Tkinter   使用Tk平台。很容易得到。半标准。[website](http://wiki.python.org/moin/TkInter)
- wxpython  基于wxWindows。跨平台越来愈流行。[website](http://wxpython.org)
- PythonWin 只能在windows上使用。使用了本机的windows GUI功能[website](http://starship.python.net/crew/mhammond)
- Java Swing    只能用于Jython。使用本机的Java GUI
- PyGTK 使用GTK平台在Linux上很流行。
- PyQT  使用Qt平台，跨平台。

py2exe
打包成windows下的可执行程序。
setup.py
```python
import distutuils
import py2exe
distutils.core.setup(windows=['wxTest.py'])
```

都编辑好后，将wxTest.py和setup.py放到一个目录下。
```python
setup.py py2exe
```

如果在运行时报以下错误：
error: MSVCP90.dll: No such file or directory
是因为没有找到MSVCP90.dll，在windows目录下搜索MSVCP90.dll这个文件，然后拷到python安装目录的DLLs下就可以了。
当打包PyQt项目时，可能会报以下错误
ImportError: No module named sip
这时只需要在打包时加上--includes sip就行啦，如：
```python
setup.py py2exe --includes sip
```