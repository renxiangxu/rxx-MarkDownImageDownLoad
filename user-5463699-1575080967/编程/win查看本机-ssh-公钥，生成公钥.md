查看 ssh 公钥方法：

1.通过命令窗口
a. 打开你的 git bash 窗口

b. 进入 .ssh 目录：cd ~/.ssh

c. 找到 id_rsa.pub 文件：ls

d. 查看公钥：cat id_rsa.pub 或者 vim id_rsa.pub

![image.png](https://upload-images.jianshu.io/upload_images/5463699-494c97102fc6b8c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

或者你也可以直接输入命令 ：cat ~/.ssh/id_rsa.pub
![image.png](https://upload-images.jianshu.io/upload_images/5463699-ac463ee3cbb2af70.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


或者你也可以直接打开你用户（一般都是 Administrator）下的 .ssh 文件夹，打开它里面的 id_rsa.pub 文件，如图：
![image.png](https://upload-images.jianshu.io/upload_images/5463699-be2c6d34c57dcf71.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

何谓公钥
1.很多服务器都是需要认证的，ssh认证是其中的一种。在客户端生成公钥，把生成的公钥添加到服务器，你以后连接服务器就不用每次都输入用户名和密码了。
2.很多git服务器都是用ssh认证方式，你需要把你生成的公钥发送给代码仓库管理员，让他给你添加到服务器上，你就可以通过ssh自由地拉取和提交代码了。
生成公钥
1.如果通过上面的方式找不到公钥，你就需要先生成公钥了：ssh-keygen
2.接着会确认存放公钥的地址，默认就是上面说的路径，直接enter键确认
3.接着会要求输入密码和确认密码，如果不想设置密码直接不输入内容 按enter键
![image.png](https://upload-images.jianshu.io/upload_images/5463699-d437ba562d0a6552.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




