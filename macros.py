#!/usr/bin/python
#coding: utf-8

import globalcache
from time import sleep
import threading


class Macros(object):
    def __init__(self):
        self.thread_limiter = threading.BoundedSemaphore(10)
        self.marantz = globalcache.Receiver()
        self.tv = globalcache.Television()
        self.cable_box = globalcache.CableBox()
        self.tv_on = False
        self.cable_box_on = False
        return

    def all_off(self):
        self.thread_limiter.acquire()
        threading.Thread(target=self._all_off).start()
        self.thread_limiter.release()
        return

    def _all_off(self):
        self.marantz.standby()
        if self.tv_on:
            self.tv.power_on_toggle()
            self.tv_on = False
        if self.cable_box_on:
            self.cable_box.power_on_toggle()
            self.cable_box_on = False
        return

    def all_on(self):
        self.marantz.power_on()
        if not self.tv_on:
            self.tv.power_on_toggle()
            self.tv_on = True
        if not self.cable_box_on:
            self.cable_box.power_on_toggle()
            self.cable_box_on = True
        sleep(3)
        return

    def movie_mode(self):
        self.thread_limiter.acquire()
        threading.Thread(target=self._movie_mode).start()
        self.thread_limiter.release()
        return

    def _movie_mode(self):
        self.marantz.power_on()
        self.marantz.select_aux1()
        if not self.tv_on:
            self.tv.power_on_toggle()
            self.tv_on = True
        if not self.cable_box_on:
            self.cable_box.power_on_toggle()
            self.cable_box_on = True
        return

    def tv_mode(self):
        self.thread_limiter.acquire()
        threading.Thread(target=self._tv_mode).start()
        self.thread_limiter.release()
        return

    def _tv_mode(self):
        self.all_on()
        self.marantz.select_sat()
        self.cable_box.discovery()
        return

    def sonos_mode(self):
        self.thread_limiter.acquire()
        threading.Thread(target=self._sonos_mode).start()
        self.thread_limiter.release()
        return

    def _sonos_mode(self):
        self.marantz.power_on()
        self.marantz.select_tv()
        return

    def tv_toggle(self):
        self.tv.power_on_toggle()
        return

    def cable_box_toggle(self):
        self.cable_box.power_on_toggle()
        return
