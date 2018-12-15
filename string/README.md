1. 长字符串: 三个单引号或三个双引号。在字符串中可以直接使用单引号或双引号，而不需要转义
``` python
print '''This is a very long string.
It continues here.
And it's not over yet.
"Hello, world!"
Still here'''
```

2. 原始字符串：
   - 以r开头
   - 不能在原始字符串的末尾输入反斜线
``` python
>>> print 'C:\\windows'
C:\windows 
# 这里并没直接打印出'C:\\windows' ;因为这里把反斜线作为特殊字符处理了。为了直接输出，需要使用原始字符串进行输出
print r'C:\\windows'
C:\\windows
```

3. unicode 字符串
``` python
print u'Andy爱Smily'
```

4. 字符串格式化

## 字符串方法
1. find
2. join
3. lower
4. replace
5. split
6. strip
7. translate