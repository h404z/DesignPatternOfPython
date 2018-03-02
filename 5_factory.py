#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/3/3
# @Author: h404z

"""定义一个用于创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化延迟到其子类"""


class LeiFeng(object):
    def sweep(self):
        print('Lei Feng sweep!')


class Student(LeiFeng):
    def sweep(self):
        print('Student sweep!')


class Volunteer(LeiFeng):
    def sweep(self):
        print('Volunteer sweep!')


class LeifengFactory(object):
    @classmethod
    def create_obj(cls):
        return LeiFeng()


class StudentFactory(object):
    @classmethod
    def create_obj(cls):
        return Student()


class VolunteerFactory(object):
    @classmethod
    def create_obj(cls):
        return Volunteer()


if __name__ == '__main__':
    s = StudentFactory.create_obj()
    s.sweep()
    v = VolunteerFactory.create_obj()
    v.sweep()
    pass
