```
![avatar](/home/picture/1.png)
```
但是
如果你的markdown在一个文件目录下，需要添加另一个目录下的图片，绝对路径是不可行的。需要 “迂回”
所谓 迂回，即需要先用../../命令返回上一文件目录，直至可以顺利找到要添加图片的目录。

举个栗子
比如你的markdown在~/Document/mymarkdown/test下，需要添加~/Downloads/Pic/background目录下的sunlight.jpg
你需要做的是

```
![](../../../Downloads/Pic/background/sunlight.jpg)
```
