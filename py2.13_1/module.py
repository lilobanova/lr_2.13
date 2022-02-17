#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fun import fun1

if __name__ == "__main__":
    tag = input("Введите тег: ").split()
    s = input("Введите строку: ").split()
    print(fun1(tag)(s))