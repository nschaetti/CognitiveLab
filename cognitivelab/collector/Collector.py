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


# Base class for Collector classes
class Collector(object):
    """
    Base classes for the other Collector classes
    """

    # Collector status
    COLLECTOR_NOT_INITIALIZED = 0
    COLLECTOT_INITIALIZED = 1

    # Constructor
    def __init__(self, *args, **kwargs):
        """
        Constructor
        :param args: Positional arguments
        :param kwargs: Arguments
        """
        pass
    # end __init__

    # region PUBLIC

    # Init the collector
    def init(self):
        """
        Init the collector
        """
        pass
    # end init

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

# end Collector
