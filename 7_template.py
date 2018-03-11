#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :2018/3/11
# @Author: h404z

"""定义一个操作中的算法骨架，将一些步骤延迟至子类中"""


class TestPaper(object):

    def question_a(self):
        print("question a: What's your name?")
        print(self.answer_a())

    def question_b(self):
        print("question b: How old are you?")
        print(self.answer_b())

    def answer_a(self):
        return ""

    def answer_b(self):
        return ""


class TestPaperA(TestPaper):
    def answer_a(self):
        return "John"

    def answer_b(self):
        return 20


class TestPaperB(TestPaper):
    def answer_a(self):
        return "Elena"

    def answer_b(self):
        return 28


if __name__ == '__main__':
    s1 = TestPaperA()
    s2 = TestPaperB()
    print("student 1")
    s1.question_a()
    s1.question_b()
    print("student 2")
    s2.question_a()
    s2.question_b()
    pass
