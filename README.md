# 将一个彩色图片转换为黑白图片 #
## 通过PIL和numpy实现 ##

---

### 调用方式 ###
控制台输入
~~~bash
python Color-to-Gray.py
~~~
或直接双击启动

---

### 启动后操作 ###
~~~bash
Set half value (Default : 100) >: 
~~~
输入分界值，默认100

---

~~~bash
Set Model (max, min) (Default : min) >:
~~~
输入最大或最小模式

若选最大模式

代码会选择图形RGB三个颜色值中的最大者与分界值比较

若比分界值大，则输出为白色

若比分界值小或相等，则输出为黑色

若选最小模式

代码会选择RGB三个颜色值中的最小者与分界值比较

其余与最大值相同

---

~~~bash
File Name >: 
~~~
如果你的图片在Python代码目录

你只需输入文件名（需要扩展名）

如果不在，请输入完整路径

如果未找到文件，会输出

~~~bash
File Not Found!
~~~

---

~~~bash
Smooth (y, n) (Default : y) >: 
~~~

是否使用图片平滑处理

算法详解见后文

---

~~~bash
Input smooth level (Default : 5) >: 
~~~

输入平滑算法平滑等级

其余见后文算法详解

---
---

### 算法详解 ###

~~~python
for _ in range(level):
    for x in range(map_img.shape[0]):
        for y in range(map_img.shape[1]):
            if not (min(map_img[x][y]) == 255):
                try:
                    conut = ((max(map_img[x + 1][y]) / 255) + (max(map_img[x - 1][y]) / 255) + (max(map_img[x][y + 1]) / 255) + (max(map_img[x][y - 1]) / 255))
                except IndexError:
                    conut = 0
                v = min(int(255 / 4 * conut), 255)
                img[x][y][0] = v
                img[x][y][1] = v
                img[x][y][2] = v
~~~