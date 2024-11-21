"""PQI
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
"""
"""
     _ __      _,.---._      .=-.-.
  .-`." ,`.  ,-." - ,  `.   /==/_ /
 /==/, -   \/==/ ,    -  \ |==|, |
|==| _ .=. |==| - .=.  ,  ||==|  |
|==| , "=",|==|  : ;=:  - ||==|- |
|==|-  ".."|==|,  "="  ,  ||==| ,|
|==|,  |    \==\ _   -    ;|==|- |
/==/ - |     ".=".  ,  ; -\/==/. /
`--`---"       `--`--"" `--`--`-`
                ---- A Terminal Tools For Python
"""

import os
import re
import sys
import pickle
import platform
from docopt import docopt
try:
    import configparser
except:
    import ConfigParser as configparser

FILE_NAME = "~\\pip\\pip.ini" if ("Windows" in platform.system()) else "~/.config/pip/pip.conf"
FILE_PATH = os.path.expanduser(FILE_NAME)
dir_path = os.path.dirname(FILE_PATH)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
SOURCES_NAME = os.path.join(dir_path, "sources.dict")
SOURCES = dict()

if not os.path.exists(SOURCES_NAME):
    with open(SOURCES_NAME, "wb") as fp:
        pickle.dump({
            "pypi": "https://pypi.python.org/simple/",
            "tuna": "https://pypi.tuna.tsinghua.edu.cn/simple",
            "douban": "https://pypi.doubanio.com/simple/",
            "aliyun": "https://mirrors.aliyun.com/pypi/simple/",
            "ustc": "https://mirrors.ustc.edu.cn/pypi/web/simple"
        }, fp)
with open(SOURCES_NAME, "rb") as fp:
    SOURCES = pickle.load(fp)

APP_DESC = """
         PQI
          ---- A Terminal Tools For Python
          @author Hangfeng Yang (https:/github.com/yhangf)
                        last_update 2023-04-10 19:27
"""

def list_all_source():
    print('\n')
    for key in SOURCES.keys():
        print(key, '\t', SOURCES[key])
    print('\n')

def write_file(source_name):
    with open(FILE_PATH, 'w') as fp:
        str_ = "[global]\nindex-url = {0}\n[install]\ntrusted-host = {1}".format(
            SOURCES[source_name], SOURCES[source_name].split('/')[2])
        fp.write(str_)

def select_source_name(source_name):
    if source_name not in SOURCES.keys():
        print("\n{} is not in the Source list.\n".format(source_name))
    else:
        write_file(source_name)
        print("\nSource is changed to {}({}).\n".format(source_name, SOURCES[source_name]))

def show_current_source():
    if not os.path.exists(FILE_PATH):
        print("\nCurrent source is pypi.\n")
        return
    config = configparser.ConfigParser()
    config.read(FILE_PATH)
    index_url = config.get("global", "index-url")
    for key in SOURCES.keys():
        if index_url == SOURCES[key]:
            print("\nCurrent source is {}({}).\n".format(key, index_url))
            break
    else:
         print("\nCurrent source is {}.\n".format(index_url))

def check_url(url):
    p = re.compile("^https?://.+?/simple/?$")
    if p.match(url) == None:
        return False    
    return True

def add_source(source_name, source_url):
    if not check_url(source_url):
        print("\nURL({}) does not conform to the rules.\n".format(source_url))
        return
    SOURCES[source_name] = source_url
    with open(SOURCES_NAME, "wb") as fp:
        pickle.dump(SOURCES, fp)
    print("\n{}({}) is add to Source list.\n".format(source_name, source_url))

def remove_source(source_name):
    if source_name not in SOURCES.keys():
        print("\n{} is not in the Source list.\n".format(source_name))
    else:
        source_url = SOURCES.pop(source_name)
        with open(SOURCES_NAME, "wb") as fp:
            pickle.dump(SOURCES, fp)
        print("\n{}({}) is remove to Source list.\n".format(source_name, source_url))

def main():
    arguments = docopt(__doc__, version="3.0.0")
    if arguments["ls"]:
        list_all_source()
    elif arguments["use"]:
        select_source_name(arguments["<name>"])
    elif arguments["show"]:
        show_current_source()
    elif arguments["add"]:
        add_source(arguments["<name>"], arguments["<url>"])
    elif arguments["remove"]:
        remove_source(arguments["<name>"])
    else:
        print("input error!")

if __name__ == "__main__":
    print(APP_DESC)
    main()
