#!/usr/bin/env python
# -*- coding: utf8 -*-
from time import sleep


def routine_1(x, eStart, eFinish, time):
    for i in range(time):
        eStart.wait()
        print x.toUtf8()
        # if x.time >= 4:
        #    x.status = 5
        sleep(1)

    eStart.clear()
    eFinish.set()
