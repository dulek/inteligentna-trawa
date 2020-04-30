# -*- coding: utf-8 -*-

from abc import ABC

from inteligentna_trawa.sensors import base

class LogicSensor(base.Sensor, ABC):
    def __init__(self, *sensors):
        self.sensors = sensors


class And(LogicSensor):
    def is_active(self):
        return all((sensor.is_active() for sensor in self.sensors))


class Or(LogicSensor):
    def is_active(self):
        return any((sensor.is_active() for sensor in self.sensors))
