# coding:utf-8
import string
import os
from PIL import Image
import time
import threading


def decimal_26(_int, c=''):
    a, b = divmod(_int-1, 26)
    c = get_case(b) + c
    if a:
        decimal_26(a, c=c)
    else:
        print(c)
    # a = _int
    # b = ''
    # while a:
    #     b = get_case((a-1) % 26) + b
    #     a = (a-1)/26
    # print b
def get_case(_int):
    for i, j in enumerate(string.ascii_uppercase):
        if i == _int:
            return j
def get_num(_letter):
    for i, j in enumerate(string.ascii_uppercase):
        if j == _letter:
            return i+1
# while True:
#     x = input(' 输入任意长字母:')
#     y = 0
#     for i, j in enumerate(reversed(list(map(get_num, x)))):
#         y += j*(26**i)
#     print(y)


# while True:
#     x = input('输入任意数字:')
#     decimal_26(int(x))
array = [1, 2, 3, 6, 5, 4]
def bubblesort():
    for i in range(len(array)):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)
# def bubblesort2():
#     for i in range(len(array)-1):
#         if array[i] > array[i+1]:
#             array[i], array[i+1] = array[i+1], array[i]
    print(array)
def bubblesort3():
    for i, j in enumerate(array):
        if i:
            if j < array[i-1]:
                array[i], array[i-1] = array[i-1], j
    print(array)
def sort():
    array = [1, 2, 4, 2, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
    array.sort()
    last_one = array[0]
    for i in range(len(array)-2, -1,  -1):
        if array[i] == last_one:
            del array[i]
        else:
            last_one = array[i]
    print(array)
def testfunc():
    temp = [lambda x: i*x for i in range(4)]
    return temp
# for i in testfunc():
#     print(i(1))
def func(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)
# func(2)
# func(2, [3,2])
# func(3)
def pil():
    unitHeight = 220
    unitWidth = 940


class FooParent:
    def __init__(self):
        self.parent = 'i\'m the parent'
        print('parent')

    def bar(self, message):
        print('{} from parent'.format(message))


class FooChild(FooParent):
    '''
    类的继承及多继承，super()的方法解决多继承问题，子类方法属性将父类覆盖之后仍可访问之
    '''
    def __init__(self):
        super().__init__()
        print('child')

    def bar(self, message):
        super().bar(message)
        print('child bar fuction')
        print(self.parent)

import functools

def wrap_1(f):
    print('f1_out')
    def inner_foo(foo):
        print('f1_in')
        return f(foo)
    return inner_foo

# @wrap_1
def wrap_2(f):
    print('f2')
    return f
    # print('f2_out')
    # def inner_foo():
    #     print('f2_in')
    #     f()
    # return inner_foo


# @wrap_2
def foo():
    print('foo')
    
def runtime(f):
    def wrap(*args):
        start = time.time()
        print(f(*args))
        end = time.time()
        print('耗时{}s'.format(end - start))
    return wrap

# 斐波那契递归解决
def memo(foo):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = foo(*args)
        return cache[args]
    return wrap


@memo
def fib_recursion(n):
    if n <= 2:
        return n
    return fib_recursion(n-1) + fib_recursion(n-2)

# @memo
# def fib_x_recursion(n):
#     if n <= 2:
#         return n
#     return 2*fib_x_recursion(n-1)


# 循环解决
def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


# def fib_x_loop(n):
#     a = 1
#     for _ in range(n-1):
#         a = a*2
#     return a


@runtime
def find(l, x):
    m = len(l)
    n = len(l[0])
    row = 0
    column = n-1
    while row < m and column >= 0:
        value = l[row][column]
        if value == x:
            return True
        elif value > x:
            column -= 1
        elif value < x:
            row += 1
    return False

#去重
# list(set(l))
# {}.fromkeys(l).keys()
# list(set(l)).sort(key=l.index)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swap_pairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swap_pairs(next.next)
            next.next = head
            return next
        return head


# 合并有序列表
# 循环
def loop_merge_sort(l1, l2):
    tmp = []
    while l1 != [] and l2 != []:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp

# 递归
def recursion_merge_sort(l1, l2, tmp=None):
    if tmp is None:
        tmp = []
    if l1 == [] or l1 == []:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return recursion_merge_sort(l1, l2, tmp)

# pop
def list_merge_sort(l1, l2):
    tmp = []
    while l1 != [] and l2 != []:
        if l1[0] < l2[0]:
            tmp.append(l1.pop(0))
        else:
            tmp.append(l2.pop(0))
    while l1:
        tmp.append(l1.pop(0))
    while l2:
        tmp.append(l2.pop(0))
    return tmp

# 二分查找 非递归
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)//2
        value = list[mid]
        if item == value:
            return True
        elif item > value:
            low = mid + 1
        else:
            high = mid - 1
    return False

# 二分查找 递归
def binary_search_recursion(l, k):
    _len = len(l)
    if _len < 1:
        return False
    mid = _len//2
    if l[mid] == k:
        return True
    elif l[mid] < k:
        return binary_search_recursion(l[mid+1:], k)
    elif l[mid] > k:
        return binary_search_recursion(l[:mid], k)


# 快排
def quick_sort(l):
    if len(l) < 2:
        return l
    else:
        key = l[0]
        less_list = [i for i in l[1:] if i < key]
        bigger_list = [i for i in l[1:] if i > key]
        return quick_sort(less_list)+[key]+quick_sort(bigger_list)

# 单例模式-装饰器
def singleton(cls):
    instance = {}
    def wrap(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrap


def singleton1(cls):
    def wrap(*args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(*args, **kwargs)
        return cls._instance
    return wrap

# 单例模式-new魔术方法
# 如有__init__方法，必须加入判断_first_init确保不会再次初始化实例
class Singleton:
    _instance_lock = threading.Lock()
    # _first_init = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                cls._instance = super().__new__(cls)
        return cls._instance


class Singleton1:
    _instance = {}
    _first_init = True

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]

# 元类metaclass
class MetaClass(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Test(metaclass=MetaClass):
    def __init__(self, num):
        # if self._first_init:
        self.num = num
        self._first_init = False

# SIMPLE ORM
class Filed:
    def __init__(self, name, content_type):
        self.content_type = content_type
        self.name = name


class String(Filed):
    def __init__(self, name):
        super().__init__(name, 'varchar')


class Integer(Filed):
    def __init__(self, name):
        super().__init__(name, 'integer')


class ModelMateClass(type):
    def __new__(cls, name, bases, kwargs):
        if name == 'Model':
            return super().__new__(cls, name, bases, kwargs)
        mapping = {}
        for k, v in kwargs.items():
            if isinstance(v, Filed):
                mapping[k] = v
        for k in mapping:
            kwargs.pop(k)
        kwargs['_mapping'] = mapping
        return super().__new__(cls, name, bases, kwargs)


class Model(dict, metaclass=ModelMateClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('"Model" object has no attribute "%s"' % item)

    def __setattr__(self, key, value):
        self[key] = value

    def creat(self):
        column = []
        args = []
        holder = []
        for k, v in self._mapping.items():
            column.append(v.name)
            args.append(getattr(self, k, None))
            holder.append('?')
        sql = 'INSERT INTO {}({}) VALUES ({})'.format(self.__tablename__, ','.join(column), ','.join(holder))
        args = str(args)
        print(sql, args)


class User(Model):
    __tablename__ = 'users'
    name = String('name')
    age = Integer('age')
    password = String('pwd')


# # 异步并发simple
# import socket
#
# sockets = {}
# for i in range(100):
#     s = socket.socket()
#     sockets[s.fileno()] = s
#     s.setblocking(False)
#     try:
#         s.connect(('aljun.me', 80))
#     except socket.error as e:
#         pass
# import select
#
# while sockets:
#     fds = select.select([], list(sockets.keys()), [])[1]
#     for fd in fds:
#         s = sockets.pop(fd)
#         print('%d connected to %s:%d' % ((fd,) + s.getpeername()))
def lazy_sum(*args):
    return lambda: sum(args)

# 协程 异步IO
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consumer {}'.format(n))
        r = '200 ok'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('producing {}'.format(n))
        r = c.send(n)
        print('consumer return {}'.format(r))
    c.close()


# asyncio

# 排列组合
# 归并排序
# def merge_sort()

if __name__ == '__main__':
    # fib = lambda n: n if n <= 2 else fib(n-1)+fib(n-2)
    # fib = lambda n: n if n <= 2 else 2*fib(n-1)
    # print(fib_loop(500))
    # find([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 5)
    # user = User(name='z', age='18', password='zzz')
    # user.name = 'zr'
    # user.creat()
    # a = lazy_sum(1,1)
    # print(a, a())
    # c = consumer()
    # producer(c)

    # import asyncio
    # @asyncio.coroutine
    # def hello(host):
    #     print(host)
    #     connect = asyncio.open_connection(host, 80)
    #     reader, writer = yield from connect
    #     writer.write(('GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host).encode('utf-8'))
    #     yield from writer.drain()
    #     while True:
    #         line = yield from reader.readline()
    #         if line == b'\r\n':
    #             break
    #         print(host, line.decode('utf-8').strip())
    #     writer.close()
    #
    # loop = asyncio.get_event_loop()
    # tasks = [hello(i) for i in ['www.baidu.com', 'www.google.com']]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    # print(binary_search_recursion([1,2,3,6,9], 1))
    list1 = os.listdir(r"F:\IDM\新建文件夹\新建文件夹")
    for i in list1:
        list2 = list1
        list2.remove(i)
        for j in list2:
            tmp = []
            tmp.extend([x for x in i if x in j])
            if len(tmp) > len(i)*9 // 10:
                print(i)


