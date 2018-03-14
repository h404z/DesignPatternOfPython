#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/3/14
# @Author: h404z

"""定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，当主题对象状态发生变化时会通知所有观察者。"""


class Observer(object):
    def __init__(self, name, subscribe):
        self.name = name
        self.subscribe = subscribe
        pass

    def update(self):
        pass

    pass


class StockObserver(Observer):
    def update(self):
        print("%s: %s stop watching stock" % (self.name, self.subscribe.action))

    pass


class NbaObserver(Observer):
    def update(self):
        print("%s: %s stop watching NBA" % (self.name, self.subscribe.action))

    pass


class SecretaryBase(object):
    def __init__(self):
        self.observers = []

    def notify(self):
        pass

    def attach(self):
        pass

    pass


class Secretary(SecretaryBase):
    def attach(self, new_observer):
        self.observers.append(new_observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


if __name__ == '__main__':
    secretary = Secretary()
    secretary.action = 'Warning! Boss is coming!'
    worker_a = StockObserver('Jack', secretary)
    worker_b = NbaObserver('David', secretary)
    secretary.attach(worker_a)
    secretary.attach(worker_b)
    secretary.notify()
    pass
