## 获取页面

- getHtml(url)
- urllib.urlopen()方法打开一个URL地址
- read()方法读取URL的数据

## 筛选页面中的数据

- getImg(html)方法
- reg = r'src="(.+?\.jpg)" alt'

## 将页面筛选的数据保存到本地

将筛选出来的图片地址通过循环遍历保存到本地
- urllib.urlretrieve()方法

## 正则表达式

- 通配符 .
- 特殊字符转义，‘python\\.org'转义.通配符，这样就只会匹配'python.org'而不会匹配'pythonzorg'等。
- 字符集[]，中括号来创建字符集
    - '[a-z]'匹配a到z的任意一个字符
    - '[a-zA-Z0-9']匹配任意大小写字母和数字
    - 反转字符集，开头使用^，'[^abc]'匹配任何除了a/b/c以外的字符
- 选择符，使用选择项的特许字符：管道符号'|'。'python|perl'只匹配python和perl
- 子模式，只对模式的一部分使用选择符，'p(ython|erl)'
- 可选项，子模式后面加上?，变成可选项。可能出现在匹配字符串。r'(http://)?(www\.)?python\.org'，匹配下列字符：
    - 'http://www.python.org'
    - 'http://python.org'
    - 'www.python.org'
    - 'python.org'
- 重复子模式
    - (pattern)*:允许模式重复0次或多次
    - (pattern)+:允许模式重复1次或多次
    - (pattern){m,n}:允许模式重复m~n次
    - 例如：
r'w*\.python\.org'匹配'www.python.org'、'.python.org'、'wwwwwwww.python.org'
r'w+\.python\,org'匹配'w.python.org';但不匹配'.python.org'
r'w{3,4}\.python\.org'只能匹配'www.python.org'和'wwww.python.org'

## re模块的内容

一些重要函数：

| 函数        | 描述    |
| ---------------------- | --------------------:   |
| compile(pattern[,flags]) | 在字符串中寻找模式 |
| search(pattern, string[,flags]) | 在字符串的开始处匹配模式 |
| split(pattern,string[,maxsplit=0]) | 根据模式的匹配项来分隔字符串 |
| findall(pattern,string) | 列出字符串中模式的所有匹配项 |
| sub(pat,repl,string[,count=0]) | 将字符串中所有pat匹配项用repl替换 |
| escape(string) | 将字符串所有特殊正则表达式字符转义 |

- re.compile将正则表达式转换为模式对象，更有效匹配
- re.search会在给定字符串中寻找第一个匹配给正则表达式的字符串中。找到放回MathObject值为True，否则返回None值为False。可用于条件语句中。
- re.match会在给定字符串的开头匹配。
    - re.match('p', 'python') 真
    - re.match('p', 'www.python') 假
- re.split会根据模式的匹配项来分割字符串
```
>>> import re
>>> some_text = 'alpha , beta ,,,gamma delta '
>>> re.split('[,]+',some_text)
['alpha ', ' beta ', 'gamma delta ']
```
- re.findall以列表形式返回给定模式的所有匹配项。比如，查找所有单词：
```
>>> import re
>>> pat = '[a-zA-Z]+'
>>> text = '"Hm...err -- are you sure?" he said, sounding insecure.'
>>> re.findall(pat,text)
['Hm', 'err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
```
- re.sub，使用给定的替换内容将匹配模式的字符串（最左端并且重叠子字符串）替换掉。
```
>>> import re
>>> pat = '{name}'
>>> text = 'Dear {name}...'
>>> re.sub(pat, 'Mr. Gumby',text)
'Dear Mr. Gumby...'
```
- re.escape，对字符串中所有可能被解释为正则运算符的字符进行转义的应用函数。如果字符串很长且包含很多特殊字符，而又不想输入很多反斜线，可以使用：
```
>>> re.escape('www.python.org')
'www\\.python\\.org'
>>> re.escape('but where is the ambiguity?')
'but\\ where\\ is\\ the\\ ambiguity\\?'
```

## 匹配对象和组
- 组，放置在圆括号里的子模块，组的序号取决于它左侧的括号组。组0就是整个模块。
    - 'There (was a (wee) (cooper)) who (lived in Fyfe)'包含组有：
    - 0 There was a wee cooper who lived in Fyfe
    - 1 was a wee cooper
    - 2 wee
    - 3 cooper
    - 4 lived in Fyfe

re匹配对象的重要方法：

- group([group1,...]),获取给定子模式（组）的匹配项
- start([group]),返回给定组的匹配的开始位置
- end([group]),返回给定组的匹配项的结束位置
- span([group]),返回一个组的开始结束位置

```
>>> import re
>>> m = re.match(r'www\.(.*)\..{3}','www.python.org')
>>> m.group()
'www.python.org'
>>> m.group(0)
'www.python.org'
>>> m.group(1)
'python'
>>> m.start(1)
4
>>> m.end(1)
10
>>> m.span(1)
(4, 10)
```