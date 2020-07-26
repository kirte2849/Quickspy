# 控制台操作



#### 获取控制台大小

```python
import os
width = os.get_terminal_size().columns
height = os.get_terminal_size().lines
print("控制台宽度%d 控制台高度%d" % (width, height))
```

在windows的cmd下

- 字母和符号大小为一个单位
- 汉字为两个单位

```
hello world #11个单位
hello,world #11个单位
你好，世界 #6个单位 因为中文逗号也为2个单位
```

------

#### 改变控制台大小

```python
os.system("mode con cols=50 lines=30")
```

------

#### 控制光标移动

```
\x1b[nA]   光标上移
\x1b[nB]   光标下移
\x1b[nC]   光标右移
\x1b[nD]   光标左移
(n为字符数)
```

------

#### 清除控制台

```python
_ = os.system('cls') #windows
```

------

#### PrettyTable 控制台绘表

[python prettytable 打印表格](https://www.jianshu.com/p/82689c1e3247)

