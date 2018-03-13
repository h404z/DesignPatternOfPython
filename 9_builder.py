#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/3/13
# @Author: h404z


"""将一个复杂对象的构建(Director)与它的表示(Builder)分离，使得同样的构建过程可以创建不同的表示(ConcreteBuilder)"""


class Person(object):
    def create_head(self):
        pass

    def create_hand(self):
        pass

    def create_body(self):
        pass

    def create_foot(self):
        pass


class ThinPerson(Person):
    def create_head(self):
        print("thin head")
        pass

    def create_hand(self):
        print("thin hand")
        pass

    def create_body(self):
        print("thin body")
        pass

    def create_foot(self):
        print("thin foot")
        pass


class ThickPerson(Person):
    def create_head(self):
        print("thick head")
        pass

    def create_hand(self):
        print("thick hand")
        pass

    def create_body(self):
        print("thick body")
        pass

    def create_foot(self):
        print("thick foot")
        pass


class Director(object):
    def __init__(self, tmp):
        self.p = tmp

    def create(self):
        self.p.create_head()
        self.p.create_body()
        self.p.create_hand()
        self.p.create_foot()


if __name__ == '__main__':
    p = ThinPerson()
    d = Director(p)
    d.create()

    pass
