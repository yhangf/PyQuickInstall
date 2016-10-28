"""PYQS
Usage:
  pyqs.py ls
  pyqs.py use <name>
  pyqs.py show
  pyqs.py (-h | --help)
  pyqs.py (-v | --version)
Options:
  -h --help        Show this screen.
  -v --version     Show version.
"""

from __future__ import print_function

import os
import re
import sys
from docopt import docopt
try:
    import configparser
except:
    import ConfigParser as configparser


SOURCES = {
    "pypi": "https://pypi.python.org/simple/",
    "tuna": "https://pypi.tuna.tsinghua.edu.cn/simple",
    "douban": "http://pypi.douban.com/simple/",
    "aliyun": "http://mirrors.aliyun.com/pypi/simple/"
}

def list_all_source():
    print("\n")
    for key in SOURCES:
        print(key, "\t", SOURCES[key])
    print("\n")

def write_file(name):
    path = os.path.expanduser("~/.pip/pip.conf")
    file_ = os.path.dirname(path)
    if not os.path.exists(file_):
        os.mkdir(file_)
    with open(path,'w') as fp:
        str_ = "[global]\nindex-url = %s\n[install]\ntrusted-host = %s"%(
            SOURCES[name], SOURCES[name].split('/')[2])
        fp.write(str_)

def select_source_name(name):
    if name not in SOURCES.keys():
        print("\nSource name is not in the list.\n")
    else:
        write_file(name)
        print("\nSource is changed to %s.\n"%(name))

def show_current_source():
    config = configparser.ConfigParser()
    path = os.path.expanduser("~/.pip/pip.conf")
    config.read(path)
    index_url = config.get("global", "index-url")
    for key, _ in SOURCES.items():
        if index_url == SOURCES[key]:
            print("\nCurrent source is %s\n"%key)
            break
    else:
         print("\nUnknown source\n")

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.1')
    if arguments['ls']:
        list_all_source()
    elif arguments['use']:
        select_source_name(arguments['<name>'])
    elif arguments['show']:
        show_current_source()
    else:
        print('input error!')
