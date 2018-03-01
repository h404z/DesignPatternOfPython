#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/3/1
# @Author: h404z

"""为其他对象提供一种代理，以控制这个对象的访问"""


class Interface(object):
    def Request(self):
        return 0


class RealSubject(Interface):
    def Request(self):
        print("Real Request")


class Proxy(Interface):
    def __init__(self):
        self.real = RealSubject()

    def Request(self):
        self.real.Request()


if __name__ == '__main__':
    Proxy().Request()
    pass
