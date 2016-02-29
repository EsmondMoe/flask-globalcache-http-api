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
        self.marantz.volume_25()
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
        self.marantz.volume_30()
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
        self.discovery()
        return

    def hgtv(self):
        self.cable_box.ch_three()
        self.cable_box.ch_two()
        return

    def history(self):
        self.cable_box.ch_six()
        self.cable_box.ch_six()
        return

    def discovery(self):
        self.cable_box.ch_three()
        self.cable_box.ch_nine()
        return

    def fox(self):
        self.cable_box.ch_four()
        self.cable_box.ch_one()
        return

    def weather(self):
        self.cable_box.ch_four()
        self.cable_box.ch_seven()
        return

    def amc(self):
        self.cable_box.ch_five()
        self.cable_box.ch_nine()
        return

    def travel(self):
        self.cable_box.ch_six()
        self.cable_box.ch_seven()
        return

    def sonos_mode(self):
        self.thread_limiter.acquire()
        threading.Thread(target=self._sonos_mode).start()
        self.thread_limiter.release()
        return

    def _sonos_mode(self):
        self.marantz.power_on()
        self.marantz.volume_30()
        self.marantz.select_tv()
        return

    def tv_toggle(self):
        self.tv.power_on_toggle()
        return

    def cable_box_toggle(self):
        self.cable_box.power_on_toggle()
        return
