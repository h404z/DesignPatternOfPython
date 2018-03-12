#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/3/12
# @Author: h404z

"""为一组调用提供一致的接口.接口将几种调用分别组合成为两组，用户通过接口调用其中的一组。"""


class SubSysA(object):
    def method_a(self):
        print("sys a, method a")


class SubSysB(object):
    def method_b(self):
        print("sys b, method b")


class SubSysC(object):
    def method_c(self):
        print("sys c, method c")


class SubSysD(object):
    def method_d(self):
        print("sys d, method d")


class Facade(object):
    def __init__(self):
        self.sub_a = SubSysA()
        self.sub_b = SubSysB()
        self.sub_c = SubSysC()
        self.sub_d = SubSysD()

    def api_alpha(self):
        print('==api alpha==')
        self.sub_a.method_a()
        self.sub_c.method_c()
        self.sub_d.method_d()

    def api_beta(self):
        print('==api beta==')
        self.sub_d.method_d()
        self.sub_c.method_c()


if __name__ == '__main__':
    f = Facade()
    f.api_alpha()
    f.api_beta()
    pass
