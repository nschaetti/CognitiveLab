#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : MongoDBCollector.py
# Description : Experiment data collector to MongoDB
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
from pymongo import MongoClient
from .Collector import Collector


# Experiment data collector to MongoDB
class MongoDBCollector(Collector):
    """
    Experiment data collector to MongoDB
    """

    # Constructor
    def __init__(self, host, port, db_name):
        """
        Constructor
        :param host: MongoDB server hostname
        :param port: MongoDB port
        :param db_name: MongoDB database
        """
        # Super
        super(MongoDBCollector, self).__init__()

        # Properties
        self._host = host
        self._port = port
        self._db_name = db_name
        self._client = None
        self._db = None
        self._connected = False
    # end __init__

    # region PROPERTIES

    # Get host
    @property
    def host(self):
        """
        Get host
        :return: MongoDB server hostname
        """
        return self._host
    # end host

    # Set host
    @host.setter
    def host(self, value):
        """
        Set host
        :param value: New hostname
        """
        self._host = value
    # end host

    # Get port
    @property
    def port(self):
        """
        Get port
        :return: MongoDB host port
        """
        return self._port
    # end port

    # Set port
    @port.setter
    def port(self, value):
        """
        Set port
        :param value: New MongoDB port
        """
        self._port = value
    # end port

    # Get database
    @property
    def db_name(self):
        """
        Get database
        :return: MongoDB database
        """
        return self._db_name

    # end port

    # Set database
    @db_name.setter
    def db_name(self, value):
        """
        Set database
        :param value: New MongoDB database
        """
        self._db_name = value
    # end database

    # endregion PROPERTIES

    # region PUBLIC

    # Init the collector
    def init(self):
        """
        Init the collector
        """
        # Connection to MongoDB
        self._client = MongoClient("{}:{}".format(self._host, self._port))

        # Get database
        self._db = getattr(self._client, self._db_name)

        # Connected
        self._connected = True
    # end init

    # Get collector status
    def status(self):
        """
        Get collector status
        :return: Collector status as an Integer
        """
        if self._connected:
            return Collector.COLLECTOT_INITIALIZED
        else:
            return Collector.COLLECTOR_NOT_INITIALIZED
        # end if
    # end status

    # endregion PUBLIC

# end MongoDBCollector
