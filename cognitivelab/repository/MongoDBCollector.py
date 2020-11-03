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
from pymongo.errors import ConnectionFailure
from .Collector import Collector
from .CollectorFactory import collector_factory


# Experiment data collector to MongoDB
class MongoDBCollector(Collector):
    """
    Experiment data collector to MongoDB
    """

    # Constructor
    def __init__(self, connection_string):
        """
        Constructor
        :param connection_string: Connection information to MongoDB
        """
        # Super
        super(MongoDBCollector, self).__init__("mongodb", connection_string)

        # Parse information
        connection_string_schema = self.get_connection_infos(connection_string)

        # No db name?
        if connection_string_schema.path == "":
            raise Exception("Database name is empty")
        # end if

        # Properties
        self._connection_string = connection_string
        self._db_name = connection_string_schema.path[1:]
        self._client = None
        self._db = None
        self._connected = False
    # end __init__

    # region PROPERTIES

    # Get connection_string
    @property
    def connection_string(self):
        """
        Get connection_string
        :return: MongoDB server hostname
        """
        return self._connection_string
    # end connection_string

    # Set host
    @connection_string.setter
    def connection_string(self, value):
        """
        Set connection_string
        :param value: New connection_string
        """
        self._connection_string = value
    # end connection_string

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

    # Open the collector
    def open(self):
        """
        Open the collector
        """
        # Connection to MongoDB
        # self._client = MongoClient(self._host, self._port, connect=True)
        self._client = MongoClient(self._connection_string)

        # Get database
        self._db = self._client[self._db_name]

        # The ismaster command is cheap and does not require auth.
        try:
            self._client.admin.command('ismaster')
        except ConnectionFailure as e:
            raise Exception("Error: Cannot connect to the MongoDB server: {}".format(e))
        # end try

        # Connected
        self._connected = True
    # end open

    # Close the collector
    def close(self):
        """
        Close the collector
        """
        # Disconnect
        self._client.close()
        self._connected = False
    # end close

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

# Register
collector_factory.register_collector('mongodb', MongoDBCollector)
