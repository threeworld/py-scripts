# Port Scanner

### 运行截图

运行命令`python main.py -h`

![](https://github.com/threeworld/Python/blob/master/Port%20Scanner/image/2.jpg?raw=true)

运行命令`python main.py -d baidu.com -t 1200 -w 9 `

![](https://github.com/threeworld/Python/blob/master/Port%20Scanner/image/1.jpg?raw=true)

### 说明

多线程高效的端口扫描器

**python版本：3.x**

```python
-h			帮助
-d			输入的主机名
-p			设置常见的top50,100,1000端口或者自定义的端口列表，目前还没有支持自定义端口范围扫描（待             实现）
-t			设置扫描的线程数
-w			设置等待连接的最大秒数
-s			显示namp统计的最常用top50,100,1000端口
```

### 文件结构

```
|---- etc
	   |---- __init__.py
	   |---- portlist.py
|---- __init__.py
|---- main.py
|---- portScanner.py
```

