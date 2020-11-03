#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : cli.py
# Description : Base class for Collector classes (which save and recover experiment data).
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 01.11.2020 21:27:09
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
import re
from urllib.parse import urlparse


# Base class for Collector classes
class Collector(object):
    """
    Base classes for the other Collector classes
    """

    # Collector status
    COLLECTOR_NOT_INITIALIZED = 0
    COLLECTOT_INITIALIZED = 1

    # Constructor
    def __init__(self, collector_type, collector_connection_string):
        """
        Constructor
        :param collector_type: local or distant collector
        :param collector_connection_string: Connection information for the collector
        """
        # Properties
        self._collector_type = collector_type
        self._collector_connection_string = collector_connection_string
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

    # end collector_type

    # Set collector type
    @collector_type.setter
    def collector_type(self, value):
        """
        Set collector type
        :param value: New collector type
        """
        self._collector_type = value
    # end collector_type

    # Get collector_destination
    @property
    def collector_connection_string(self):
        """
        Get collector_connection_string
        :return: Collector destination
        """
        return self._collector_connection_string
    # end collector_connection_string

    # Set collector_destination
    @collector_connection_string.setter
    def collector_connection_string(self, v):
        """
        Set collector_connection_string
        :return:
        """
        self._collector_connection_string = v
    # end collector_connection_string

    # endregion PROPERTIES

    # region PUBLIC

    # Open the collector
    def open(self):
        """
        open the collector
        """
        pass
    # end open

    # Close the collector
    def close(self):
        """
        Close the collector
        """
        pass
    # end close

    # Get collector status
    def status(self):
        """
        Get collector status
        :return: Collector status as a Integer
        """
        pass
    # end status

    # Get experiment
    def get_experiment(self, experiment_name):
        """
        Get an experiment from the collector
        :param experiment_name: Experiment name
        :return: CLExperiment object
        """
        pass
    # get_experiment

    # What is the status of an experiment?
    def experiment_status(self, experiment_name):
        """
        What is the status of an experiment?
        :param experiment_name: Experiment name
        :return: Status as an integer
        """
        pass
    # end experiment_status

    # endregion PUBLIC

    # region OVERRIDE

    # Override equals
    def __eq__(self, other):
        """
        Override equals
        :param other:
        :return:
        """
        return self._collector_type == other.collector_type and \
               self._collector_connection_string == other.collector_connection_string
    # end __eq__

    # endregion OVERRIDE

    # region STATIC

    # Extract host, port and db name from connection string
    @staticmethod
    def get_connection_infos(destination):
        """
        Get connection infos
        :param destination: Destination string
        :return:
        """
        return urlparse(destination)
    # end get_connection_info

    # endregion STATIC

# end Collector
