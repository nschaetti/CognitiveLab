#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : config/objects/Collector.py
# Description : Represent a collector in the configuration
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 01.11.2020 23:44:00
# Location : Nyon, Switzerland
#
# This file is part of the CognitiveLab package.
# The CognitiveLab package is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CognitiveLab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with CognitiveLab.  If not, see <http://www.gnu.org/licenses/>.
#
# Nils Schaetti <nils.schaetti@unige.ch>
#

# Imports


# Represent a collector in the configuration
class Collector(object):
    """
    Represent a collector in the configuration
    """

    # Constructor
    def __init__(self, collector_type, collector_destination):
        """
        Constructor
        :param collector_type: Collector type
        :param collector_destination: Collector destination
        """
        # Property
        self._collector_type = collector_type
        self._collector_destination = collector_destination
    # end __init__

    # region PROPERTIES

    # Collector type
    @property
    def collector_type(self):
        """
        Get collector type
        :return: Collector type (local, distant)
        """
        return self._collector_type
    # end collectot_type

    # Set collector type
    @collector_type.setter
    def collector_type(self, value):
        """
        Set collectot type
        :param value: New collector type
        """
        self._collector_type = value
    # end collectot_type

    # endregion PROPERTIES

# end Collector
