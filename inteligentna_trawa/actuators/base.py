# -*- coding: utf-8 -*-

import abc
import time


class Actuator(abc.ABC):
    @abc.abstractmethod
    def turn_on(self):
        pass

    @abc.abstractmethod
    def turn_off(self):
        pass

    def turn_on_for(self, seconds):
        # TODO(dulek): Alright, this is dumb on many levels, fix it up once
        #              it's known how it'll be used.
        self.turn_on()
        time.sleep(seconds)
        self.turn_off()
