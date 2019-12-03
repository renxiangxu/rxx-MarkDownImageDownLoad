远程仓库设置 dev 和 master 两个分支，master 作为一个稳定版分支，可用于直接发布产品，日常的开发则 push 到 dev 分支，通过github上进行merge。

1. 克隆代码
git clone xxxxxxxx

2. 查看所有分支
git branch --all 
默认只有master分支，所以会看到如下两个分支或者三个分支，
master[本地主分支] ，origin/master[远程主分支]，head[我也不知道是什么鬼]
新克隆下来的代码默认master和origin/master是关联的，也就是他们的代码保持同步

3. 创建本地新的dev分支
git branch dev  # 创建本地分支
git branch # 查看分支
这里有master和dev，master上会有一个星号，表示当前在这个分支
目前dev只存在本地，远程仓库没有dev

4. 上传dev分支
git push origin dev:dev # github上也有dev分支了

5. 在dev分支开发代码

6.上传到github上

7.github上将dev代码merge到master上

8.本地拉代码的时候拉master分支到dev上

