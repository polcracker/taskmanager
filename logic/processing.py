#!/usr/bin/env python
# -*- coding: utf8 -*-


class Process(object):
    def __init__(
            self,
            thread=None,
            name='none',
            processor='',
            eventStart=None,
            eventFinish=None,
            eventError=None,
            priority=0,
            status=3,  # 1,
            time=4,
            resources=list()
    ):
        self.thread = thread
        self.name = name
        self.processor = processor
        self.eventStart = eventStart
        self.eventFinish = eventFinish
        self.eventError = eventError
        self.priority = priority
        self.status = status
        self.time = time
        self.resources = resources
