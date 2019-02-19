# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import pyperclip


class Main(Wox):

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
