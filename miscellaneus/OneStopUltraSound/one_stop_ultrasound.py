#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
import time
import json

import sys
import os
from TouchStyle import *
import ftrobopy
import smbus
#import struct, array, math

bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1


class TouchGuiApplication(TouchApplication):
    def __init__(self, args):
        TouchApplication.__init__(self, args)

        # create the empty main window
        w = TouchWindow("Ultra Sonido")

        # try to read TXT_IP environment variable
        txt_ip = os.environ.get('TXT_IP')
        try:
            # connect to TXT's IO controller
            self.txt = ftrobopy.ftrobopy("localhost", 65000)
        except:
            self.txt = None

        vbox = QVBoxLayout()

        if not self.txt:
            # display error of TXT could no be connected
            # error messages is centered and may span
            # over several lines
            # create the error message label
            err_msg = QLabel("Error connecting IO server")
            # allow it to wrap over several lines
            err_msg.setWordWrap(True)
            # center it horizontally
            err_msg.setAlignment(Qt.AlignCenter)
            # attach it to the main output area
            vbox.addWidget(err_msg)
        else:

            # configure all TXT outputs to normal mode
            M = [self.txt.C_OUTPUT, self.txt.C_OUTPUT,
                 self.txt.C_OUTPUT, self.txt.C_OUTPUT]
            I = [(self.txt.C_SWITCH, self.txt.C_DIGITAL),
                 (self.txt.C_SWITCH, self.txt.C_DIGITAL),
                 (self.txt.C_SWITCH, self.txt.C_DIGITAL),
                 (self.txt.C_SWITCH, self.txt.C_DIGITAL),
                 (self.txt.C_SWITCH, self.txt.C_DIGITAL),
                 (self.txt.C_SWITCH, self.txt.C_DIGITAL),
                 (self.txt.C_SWITCH, self.txt.C_DIGITAL),
                 (self.txt.C_SWITCH, self.txt.C_DIGITAL)]
            self.txt.setConfig(M, I)
            self.txt.updateConfig()

            # initialize ultrasound
            self.ultrasound = self.txt.ultrasonic(1)

            # assume initually the button is not pressed
            self.distance = 0
            self.timer = QTimer(self)                        # create a timer
            # connect timer to on_timer slot
            self.timer.timeout.connect(self.on_timer)
            # fire timer every 100ms (10 hz)
            self.timer.start(100)


        w.centralWidget.setLayout(vbox)
        w.show()
        self.exec_()

    # an event handler for the timer (also a qt slot)
    def on_timer(self):
        # change saved state to reflect input state
        self.distance = self.ultrasound.distance()
        print(self.distance)
        # toggle lamp state if button has been pressed
        if self.distance >= 11:
            print('here it comes')
            bus.write_byte(8, 5)
        elif self.distance < 11:
            print('here it should not')
            bus.write_byte(8, 0)
            sys.exit(0)

if __name__ == "__main__":
    TouchGuiApplication(sys.argv)
