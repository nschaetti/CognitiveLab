# File : config/CollectorFactory.py
# Description : Class to create and access Collector classes
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


# Class to create and access Collector classes
class CollectorFactory(object):
    """
    Class to create and access Collector classes
    """

    # Instance
    _instance = None

    # Constructor
    def __init__(self):
        """
        Constructor
        """
        # Init. collectors
        self._collectors = dict()

        # Save instance
        self._instance = self
    # end __init__

    # region PUBLIC

    # List of collector types
    def collector_types(self):
        """
        List of collector types
        :return: Collector types as a List
        """
        return self._collectors.keys()
    # end collector_types

    # Register collector
    def register_collector(self, name, collector):
        """
        Register collector
        :param name:
        :param collector:
        :return:
        """
        self._collectors[name] = collector
    # end register_collector

    # Get a collector
    def get_collector(self, collector_type, connection_string):
        """
        Get a collector
        :param collector_type:
        :param connection_string:
        :return:
        """
        # Create and returns collector
        collector = self._collectors[collector_type]
        if not collector:
            raise ValueError(collector_type)
        # end if
        return collector(connection_string)
    # end get_collector

    # Get a collector from configuration
    def get_collector_from_config(self, collector_config):
        """
        Get a collector from configuration
        :param collector_config: config.objects.Collector object
        :return:
        """
        return self.get_collector(
            collector_config.collector_type,
            collector_config.collector_destination
        )
    # end get_collector_from_config

    # Get instance
    def get_instance(self):
        """
        Get instance
        :return: Instance
        """
        return self._instance
    # end get_instance

    # endregion PUBLIC

    # region STATIC

    # endregion STATIC

# end CollectorFactory

# Create a factory
collector_factory = CollectorFactory()
