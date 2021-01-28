#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

import logging


logger = logging.getLogger(__name__)


def hello():
    u"""helloテスト"""
    # logger.info(u"hello")
    logger.debug(u"hello world")
    # logger.warn(u"hello")
    return True
