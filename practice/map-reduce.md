练习

利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
```
reg = map(lambda s: s[0].upper()+s[1:].lower(), ['admin', 'PeTer', 'cIndY', 'd'])
print reg
```

Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
```
def prod(x, y)
  return x*y
p = reduce(prod, ([1,2,3,4,5,6,7])
print p

p = reduce(lambda x,y: x*y, (l))
```
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
