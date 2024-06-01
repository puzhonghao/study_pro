#!/usr/bin/env python
#coding=utf-8

def test():
    try:
        a = 1 / 0
        print(a)
    except Exception as e:
        print("error--")

    print("hhhhhhh")

if __name__ == "__main__":
    test()