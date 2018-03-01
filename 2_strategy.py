#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/2/28
# @Author: h404z

"""
定义算法家族并且分别封装，它们之间可以相互替换且不影响客户端
商场收银软件，需要根据不同的销售策略方式进行收费
"""


class CashContext(object):
    def __init__(self, csuper):
        self.cs = csuper

    def get_result(self, money):
        return self.cs.accept_cash(money)


class CashSuper(object):
    def accept_cash(self, money):
        return 0


class CashNormal(CashSuper):
    def accept_cash(self, money):
        return money


class CashDiscount(CashSuper):
    def __init__(self, discount):
        self.discount = discount
        pass

    def accept_cash(self, money):
        return (1 - self.discount) * money

    pass


class CashRefund(CashSuper):
    def __init__(self, meet, refund):
        self.meet = meet
        self.refund = refund
        pass

    def accept_cash(self, money):
        if money >= self.meet:
            return money - self.refund
        else:
            return money

    pass


if __name__ == '__main__':
    money = int(input('money: '))
    strategy = dict()
    strategy['1'] = CashContext(CashNormal())
    strategy['2'] = CashContext(CashDiscount(0.2))
    strategy['3'] = CashContext(CashRefund(300, 100))
    choose = input("choose type::\n[1] Normal\n[2]Discount\n[3]Refund\n")
    if choose in strategy:
        final_pay = strategy[choose].get_result(money)
        print('you should pay: %s' % final_pay)
    else:
        print('strategy %s is not exists' % choose)


    pass
