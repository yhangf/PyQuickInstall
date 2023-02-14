```shell
                                         _ __      _,.---._      .=-.-.
                                      .-`.' ,`.  ,-.' - ,  `.   /==/_ /
                                     /==/, -   \/==/ ,    -  \ |==|, |  
                                    |==| _ .=. |==| - .=.  ,  ||==|  |  
                                    |==| , '=',|==|  : ;=:  - ||==|- |  
                                    |==|-  '..'|==|,  '='  ,  ||==| ,|  
                                    |==|,  |    \==\ _   -    ;|==|- |  
                                    /==/ - |     '.='.  ,  ; -\/==/. /  
                                    `--`---'       `--`--'' `--`--`-`   

                                                    ---- by Hangfeng Yang

```
# <p align="center">pqi: a terminal tools for Python:globe_with_meridians:</p>

<p align="center">
    <a href="https://github.com/yhangf/PyQuickInstall/blob/master/LICENSE">
        <img src="https://img.shields.io/cocoapods/l/EFQRCode.svg?style=flat">
        </a>
    <a href="https://pypi.python.org/pypi/pqi">
        <img src="https://img.shields.io/pypi/v/pqi.svg">
        </a>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/language-python-ff69b4.svg">
        </a>
    <a href="https://github.com/yhangf/PyQuickInstall">
    <img src="https://img.shields.io/github/stars/yhangf/PyQuickInstall.svg?style=social&label=Star">
        </a>
    <a href="https://github.com/yhangf/PyQuickInstall">
    <img src="https://img.shields.io/github/forks/yhangf/PyQuickInstall.svg?style=social&label=Fork">
        </a>
</p>
由于国内通过pip下载python包的速度真的很慢，很容易因为超时而失败，而pqi可以把PyPi源迅速切换为国内源tuna, douban, aliyun, ustc从而大大加快python包的安装速度，提速效果见下图所示。

![](https://github.com/yhangf/PyQuickInstall/blob/master/picture/db.png)

## 怎么使用(兼容py2/py3/linux/windows/MacOS)

### 1.安装
#### 方法一（推荐）

```
>>> pip install pqi
```

#### 方法二
```
>>> git clone https://github.com/yhangf/PyQuickInstall.git
>>> python3 setup.py install
```


### 2. 命令行输入 `pqi` 回车
```
>>> pqi
Usage:
  pqi ls
  pqi use <name>
  pqi show
  pqi add <name> <url>
  pqi remove <name>
  pqi (-h | --help)
  pqi (-v | --version)
Options:
  -h --help        Show this screen.
  -v --version     Show version.
```
* 列举所有支持的PyPi源
```
>>> pqi ls
```

* 改变PyPi源
```
>>> pqi use <name>
```
例子，比如运行`pqi use tuna`即把当前PyPi源改为清华的PyPi源

* 显示当前PyPi源
```
>>> pqi show
```

* 添加新的pip源(如添加USTC源）
```
>>> pqi add ustc https://mirrors.ustc.edu.cn/pypi/web/simple
```

* 移除pip源（如官方PyPi源）
```
>>> pqi remove pypi
```

### 3. 升级到最新版`pqi`
```
>>> pip install --upgrade pqi
```

## LICENSE
[MIT](https://github.com/yhangf/PyQuickInstall/blob/master/LICENSE)
