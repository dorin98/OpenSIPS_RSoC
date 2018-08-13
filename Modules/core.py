#!/usr/bin/env python3

from comm import *
#
conn = OpenSIPSCTLComm(str(__name__).upper())


def ps(args):
    # conn.execute("ps")
    print(args)


def test_func():
    pass


# print(dir())
