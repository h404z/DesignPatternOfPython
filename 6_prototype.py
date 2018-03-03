#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/3/4
# @Author: h404z

"""用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。"""

import copy


class Resume(object):
    def __init__(self, name):
        self.name = name

    def set_work_exp(self, place, year):
        self.place = place
        self.year = year
        pass

    def set_age(self, age):
        self.age = age
        pass

    def display(self):
        print("name:{0}\nage:{1}\nwork exp:{2}, {3}years\n".format(self.name, self.age, self.place, self.year))

    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    nick = Resume('Nick')
    fake_nick = nick.clone()

    nick.set_age(20)
    fake_nick.set_age(10)

    nick.set_work_exp('netease', 3)
    fake_nick.set_work_exp('google', 10)

    nick.display()
    fake_nick.display()

    pass
