#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/2/27
# @Author: h404z

"""工厂根据条件产生功能不同的类"""


class OperationFactory(object):
    @classmethod
    def create_operation(cls, op_name, op1, op2):
        operation = {
            '+': OperationAdd(op1, op2),
            '-': OperationSub(op1, op2),
            '*': OperationMul(op1, op2),
            '/': OperationDiv(op1, op2),
        }
        if op_name in operation:
            return operation[op_name]
        else:
            return Operation(op1, op2)


class Operation(object):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        pass

    def get_result(self):
        return 'original operation'


class OperationAdd(Operation):
    def get_result(self):
        return self.op1 + self.op2


class OperationSub(Operation):
    def get_result(self):
        return self.op1 - self.op2


class OperationMul(Operation):
    def get_result(self):
        return self.op1 * self.op2


class OperationDiv(Operation):
    def get_result(self):
        try:
            return self.op1 / self.op2
        except ZeroDivisionError:
            return 'error! cant divided by zero!'


class OperationUndef(Operation):
    def get_result(self):
        return 'operation undefine!'


if __name__ == '__main__':
    operator = input('operator: ')
    a = int(input('a: '))
    b = int(input('b: '))
    op = OperationFactory.create_operation(operator, a, b)
    print(op.get_result())
    pass
