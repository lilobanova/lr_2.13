#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(tag):
    def fun2(s):
        return f'<{tag}>{s}</{tag}>'
    return fun2
