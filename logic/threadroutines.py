#!/usr/bin/env python
# -*- coding: utf8 -*-
from time import sleep

from config import ERROR_TIME


def routine_1(x, eStart, eFinish, eError, time):
    eError.clear()
    for i in range(time):
        eStart.wait()
        print x.toUtf8()

        if i >= ERROR_TIME:
            eError.set()
            return

        sleep(1)

    eStart.clear()
    eFinish.set()
