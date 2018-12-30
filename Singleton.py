#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:ZRui
# datetime:2018/11/2 13:39
# software:PyCharm
import time
import threading


# TODO: 使用模块
class SingletonModule:
    """
    Python的模块是天然的单例模式，首次引入生成的pyc文件会在下次运行中保持，不再执行模块代码
    """
    def foo(self):
        pass

# 在外部模块引入即可from Singleton import singleton
singleton = SingletonModule()


# FIXME: 使用装饰器，多线程IO不适用
def singleton(cls):
    _instance = {}
    """装饰器是用Python闭包特性实现的"""
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton


@singleton
class SingletonDecorator:
    def __init__(self):
        # 加入延时模拟IO
        # time.sleep(1)
        pass


# FIXME: 使用类方法，多线程IO不适用
class SingletonClass:
    """
    实例化时用SingletonClass.instance()方法
    """
    def __init__(self):
        # time.sleep(1)
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(*args, **kwargs)
        return cls._instance


# TODO: 使用类方法，加线程锁！
class SingletonClassLock:
    """
    实例化时用SingletonClassLock.instance()方法
    """
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                cls._instance = cls(*args, **kwargs)
        return cls._instance


# TODO: 使用__new__方法（推荐）
class SingletonNew:
    """实例化时用SingleNew()即可"""
    _instance_lock = threading.Lock()
    _first_init = True

    def __init__(self):
        if self._first_init:
            self._first_init = False
        time.sleep(1)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                cls._instance = super().__new__(cls)
        return cls._instance

# def task(*args):
#     obj = SingletonNew()
#     print(obj)
# for i in range(10):
#     t = threading.Thread(target=task, args=[i,])
#     t.start()


# TODO: 基于metaclass方式实现
class SingletonType(type):
    """
    1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
    2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
    """
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self):
        pass
