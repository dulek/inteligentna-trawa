# -*- coding: utf-8 -*-

import gpiozero

from inteligentna_trawa.actuators import base


class GPIOPin(base.Actuator):
    def __init__(self, pin, active_high=True):
        self.dev = gpiozero.LED(pin=pin, initial_value=False,
                                active_high=active_high)

    def turn_on(self):
        self.dev.on()

    def turn_off(self):
        self.dev.off()
