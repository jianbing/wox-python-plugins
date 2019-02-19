# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
import types
import traceback
import logging
import functools
import os
from contextlib import contextmanager

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename="error.log",
                    filemode='a')


class Log:
    @classmethod
    def debug(cls, msg):
        logging.debug(msg)

    @classmethod
    def info(cls, msg):
        logging.info(msg)

    @classmethod
    def error(cls, msg):
        logging.error(msg)


@contextmanager
def load_module():
    try:
        yield
    except:
        Log.error(traceback.format_exc())
        os.system(r'explorer "{}"'.format(os.getcwd()))


def debug(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            error = traceback.format_exc()
            WoxAPI.show_msg("error", error)
            Log.error(error)
            os.system(r'explorer "{}"'.format(os.getcwd()))

    return wrap


class DebugMeta(type):
    def __new__(cls, clsname, bases, attrs):
        for func_name, func in attrs.items():
            if isinstance(func, types.FunctionType):
                attrs[func_name] = debug(func)
        return super(DebugMeta, cls).__new__(cls, clsname, bases, attrs)
