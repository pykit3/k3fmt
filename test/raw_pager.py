#!/usr/bin/env python2
# coding: utf-8

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    prefix = args[0]
    cont = sys.stdin.read()
    lines = cont.split("\n")
    for line in lines:
        print(prefix, line)
