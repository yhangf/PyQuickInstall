# pyqs

由于国内通过pip下载python包的速度真的很慢，而pyqs可以把PyPi源迅速切换化为国内源tuna, double, aliyun, 从而加快python包的安装速度。

## 怎么使用(兼容py2/py3)
### 1. 首先把项目克隆到本地

### ```git clone https://github.com/Fenghuapiao/PyQuickInstall.git```
然后pip安装依赖库`docopt`
```
pip install docopt
```

### 2. 进入项目文件的根目录，并打开命令行输入 ```pyqs.py ``` 回车，会显示如下帮助内容
```
Usage:
  pyqs.py ls
  pyqs.py use <name>
  pyqs.py show
  pyqs.py (-h | --help)
  pyqs.py (-v | --version)
Options:
  -h --help        Show this screen.
  -v --version     Show version.
```
列举所有支持的PyPi源
```
pyqs.py ls
```

改变PyPi源
```
pyqs.py use <name>
```
例子，比如运行```pyqs.py use tuna```即把当前PyPi源改为清华的PyPi源

显示当前PyPi源

```
pyqs.py show
```

## LICENSE
[MIT](https://github.com/Fenghuapiao/PyQuickInstall/blob/master/LICENSE)
