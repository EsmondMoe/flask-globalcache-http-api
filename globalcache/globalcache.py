#!/usr/bin/python
#coding: utf-8

import socket
import yaml
import sys


class AudioVisual(object):
    def __init__(self):
        self.config = yaml.safe_load(open("./config.yml"))
        return

    def send_command(self, *args):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print "socket creation failed with error %s" % (err)
            return 1

        try:
            s.connect((self.config['gc_config']['host_ip'], self.config['gc_config']['port']))
        except socket.error as err:
            print "socket creation failed with error %s" % (err)
            s.close()
            return 1

        for ir_code in args:
            ir_code = "".join(ir_code.split())
            ir_code = "%s\r" % ir_code
            s.send(ir_code)
            response = s.recv(24)
            if not 'completeir' in response:
                print 'error'
                continue

        s.close()
        return


class Receiver(AudioVisual):
    def power_on(self):
        self.send_command(self.config['receiver']['power_on'])
        return

    def standby(self):
        self.send_command(self.config['receiver']['standby'])
        return

    def volume_up(self):
        self.send_command(self.config['receiver']['volume_up'])
        return

    def volume_down(self):
        self.send_command(self.config['receiver']['volume_down'])
        return

    def volume_25(self):
        self.send_command(self.config['receiver']['volume_25'])
        return

    def volume_30(self):
        self.send_command(self.config['receiver']['volume_30'])
        return

    def volume_35(self):
        self.send_command(self.config['receiver']['volume_35'])
        return

    def mute_toggle(self):
        self.send_command(self.config['receiver']['mute_toggle'])
        return

    def select_sat(self):
        self.send_command(self.config['receiver']['select_sat'])
        return

    def select_tv(self):
        self.send_command(self.config['receiver']['select_tv'])
        return

    def select_aux1(self):
        self.send_command(self.config['receiver']['select_aux1'])
        return

    def select_aux2(self):
        self.send_command(self.config['receiver']['select_aux2'])
        return

    def select_game(self):
        self.send_command(self.config['receiver']['select_game'])
        return

    def select_bd(self):
        self.send_command(self.config['receiver']['select_bd'])
        return

    def select_dvd(self):
        self.send_command(self.config['receiver']['select_dvd'])
        return

    def select_cd(self):
        self.send_command(self.config['receiver']['select_cd'])
        return


class Television(AudioVisual):
    def power_on_toggle(self):
        self.send_command(self.config['television']['power_on_toggle'])
        return

    def select_hdmi(self):
        self.send_command(self.config['television']['select_hdmi'])
        return


class CableBox(AudioVisual):
    def power_on_toggle(self):
        self.send_command(self.config['cable_box']['power_on_toggle'])
        return

    def ch_up(self):
        self.send_command(self.config['cable_box']['ch_up'])
        return

    def ch_down(self):
        self.send_command(self.config['cable_box']['ch_down'])
        return

    def ch_info(self):
        self.send_command(self.config['cable_box']['ch_info'])
        return

    def ch_last(self):
        self.send_command(self.config['cable_box']['ch_last'])
        return

    def ch_one(self):
        self.send_command(self.config['cable_box']['ch_one'])
        return

    def ch_two(self):
        self.send_command(self.config['cable_box']['ch_two'])
        return

    def ch_three(self):
        self.send_command(self.config['cable_box']['ch_three'])
        return

    def ch_four(self):
        self.send_command(self.config['cable_box']['ch_four'])
        return

    def ch_five(self):
        self.send_command(self.config['cable_box']['ch_five'])
        return

    def ch_six(self):
        self.send_command(self.config['cable_box']['ch_six'])
        return

    def ch_seven(self):
        self.send_command(self.config['cable_box']['ch_seven'])
        return

    def ch_eight(self):
        self.send_command(self.config['cable_box']['ch_eight'])
        return

    def ch_nine(self):
        self.send_command(self.config['cable_box']['ch_nine'])
        return

    def ch_zero(self):
        self.send_command(self.config['cable_box']['ch_zero'])
        return

if __name__ == '__main__':
    sys.exit(0)
