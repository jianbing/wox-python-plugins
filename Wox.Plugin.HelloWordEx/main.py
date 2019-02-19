# -*- coding: utf-8 -*-
# 固定写法，导入相关类库和函数
from util import Wox, WoxAPI, load_module, Log, DebugMeta

# 统一加载模块
with load_module():
    import pyperclip


class Main(Wox, metaclass=DebugMeta):  # 固定写法

    def query(self, keyword):
        results = list()
        results.append({
            "Title": "input",
            "SubTitle": keyword,
            "IcoPath": "Images/ico.ico",
            "JsonRPCAction": {
                "method": "test_func",
                "parameters": [keyword],
                "dontHideAfterAction": False
            }
        })
        return results

    def test_func(self, keyword):
        pyperclip.copy(keyword)


if __name__ == "__main__":
    Main()
