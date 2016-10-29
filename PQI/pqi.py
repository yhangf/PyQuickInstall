"""PQI
Usage:
  pqi ls
  pqi use <name>
  pqi show
  pqi (-h | --help)
  pqi (-v | --version)
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

APP_DESC = """
         PQI
          ---- A Terminal Tools For Python
          @author Yanghangfeng (https:/github.com/Fenghuapiao)
                        last_update 2016-10-29 08:58
"""

def list_all_source():
    print("\n")
    for key in SOURCES.keys():
        print(key, "\t", SOURCES[key])
    print("\n")

def write_file(name):
    path = os.path.expanduser("~/.pip/pip.conf")
    file_ = os.path.dirname(path)
    if not os.path.exists(file_):
        os.mkdir(file_)
    with open(path,'w') as fp:
        str_ = "[global]\nindex-url = {0}\n[install]\ntrusted-host = {1}".format(
            SOURCES[name], SOURCES[name].split('/')[2])
        fp.write(str_)

def select_source_name(name):
    if name not in SOURCES.keys():
        print("\nSource name is not in the list.\n")
    else:
        write_file(name)
        print("\nSource is changed to {name}.\n".format(name=name))

def show_current_source():
    config = configparser.ConfigParser()
    path = os.path.expanduser("~/.pip/pip.conf")
    config.read(path)
    index_url = config.get("global", "index-url")
    for key in SOURCES.keys():
        if index_url == SOURCES[key]:
            print("\nCurrent source is {key}\n".format(key=key))
            break
    else:
         print("\nUnknown source\n")

def main():
    arguments = docopt(__doc__, version='1.0.1')
    if arguments['ls']:
        list_all_source()
    elif arguments['use']:
        select_source_name(arguments['<name>'])
    elif arguments['show']:
        show_current_source()
    else:
        print('input error!')

if __name__ == '__main__':
    print(APP_DESC)
    main()
