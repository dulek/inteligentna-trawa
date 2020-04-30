# -*- coding: utf-8 -*-

import abc


class Sensor(abc.ABC):
    @abc.abstractmethod
    def is_active(self):
        pass
