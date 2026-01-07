#!/usr/bin/env python2
# coding: utf-8

import sys

import k3fmt

if __name__ == "__main__":
    args = sys.argv[1:]

    pager = args.pop(0).split()
    control_char = args.pop(0) == "1"
    limit = int(args.pop(0))
    lines = args

    k3fmt.page(lines, max_lines=limit, pager=pager)
