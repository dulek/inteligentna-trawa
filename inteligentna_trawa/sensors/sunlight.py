# -*- coding: utf-8 -*-

import datetime

from pysolar import solar

from inteligentna_trawa.sensors import base


class Sunlight(base.Sensor):
    def __init__(self, lat, lon, min_az, max_az, max_alt=0.0):
        self.lat = lat
        self.lon = lon
        self.min_az = min_az
        self.max_az = max_az
        self.max_alt = max_alt

    def is_active(self):
        time = datetime.datetime.now(datetime.timezone.utc)
        az, alt = solar.get_position(self.lat, self.lon, time)

        return alt <= self.max_alt or self.min_az <= az <= self.max_az
