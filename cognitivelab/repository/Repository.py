#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : config/objects/Repository.py
# Description : Represent a repository in the configuration
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
import os
import datetime
from .Laboratory import Laboratory


# Represent a repository in the configuration
class Repository(object):
    """
    Represent a repository in the configuration
    """

    # Constructor
    def __init__(self, repo_name, repo_collectors=None, repo_depots=None, repo_creation_date=None,
                 repo_modification_date=None):
        """
        Constructor
        :param repo_name: Repository name
        :param repo_collectors: List of CollectorConfig objects
        :param repo_depots: List of remote depots
        :param repo_creation_date: Creation date of the repository
        :param repo_modification_date: Date of the last modification
        """
        # Repository name
        self._repo_name = repo_name

        # Creation and modification date
        self._creation_date = datetime.datetime.now() if repo_creation_date is None else repo_creation_date
        self._modification_date = datetime.datetime.now() if repo_modification_date is None else repo_modification_date

        # Repository collectors
        if repo_collectors is None:
            self._repo_collectors = list()
        else:
            self._repo_collectors = repo_collectors
        # end if

        # List of remote depot
        if repo_depots is None:
            self._repo_depots = list()
        else:
            self._repo_depots = repo_depots
        # end depot_list

        # Repository labs
        self._repo_labs = list()
    # end __init__

    # region PROPERTIES

    # Get repository name
    @property
    def repo_name(self):
        """
        Get repository name
        :return: Repository name
        """
        return self._repo_name
    # end repo_name

    # Set repository name
    @repo_name.setter
    def repo_name(self, value):
        """
        Set repository name
        :param value: New repository name
        """
        self._repo_name = value
    # end repo_name

    # Get collectors
    @property
    def repo_collectors(self):
        """
        Get collectors
        :return: List of CollectorConfig objects.
        """
        return self._repo_collectors
    # end repo_collectors

    # Set collectors
    @repo_collectors.setter
    def repo_collectors(self, value):
        """
        Set collectors
        :param value: New list of CollectorConfig objects.
        """
        self._repo_collectors = value
    # end repo_collectors

    # Get depots
    @property
    def repo_depots(self):
        """
        Get remote depots
        :return: List of remote depots (RemoteDepot)
        """
        return self._repo_depots
    # end repo_depots

    # Set collectors
    @repo_depots.setter
    def repo_depots(self, value):
        """
        Set remote depots
        :param value: New list of RemoteDepot objects.
        """
        self._repo_depots = value
    # end repo_depots

    # Get creation date
    @property
    def repo_creation_date(self):
        """
        Get creation date
        :return: Creation date
        """
        return self._creation_date
    # end repo_creation_date

    # Get modification date
    @property
    def repo_modification_date(self):
        """
        Get modification date
        :return: Modification date
        """
        return self._modification_date
    # end repo_modification_date

    # Set modification date
    @repo_modification_date.setter
    def repo_modification_date(self, value):
        """
        Set modification date
        """
        self._modification_date = value
    # end repo_modification_date

    # endregion PROPERTIES

    # region PUBLIC

    # Update modification date
    def update_modification_date(self):
        """
        Update modification date
        """
        self._modification_date = datetime.datetime.now()
    # end update_modification_date

    # Remove a collector
    def remove_collector(self, collector_type, collector_connection_string):
        """
        Remove a collector
        :param collector_type: Collector type
        :param collector_connection_string: Connection string for this collector
        :return:
        """
        # Target collector
        target_collector = None

        # Go through all collectors
        for collector in self._repo_collectors:
            if collector.collector_type == collector_type and \
               collector.collector_connection_string == collector_connection_string:
                target_collector = collector
            # end if
        # end for

        # Remove from list
        if target_collector is not None:
            self._repo_collectors.remove(target_collector)
        else:
            raise Exception("Cannot remove collector, not found in repository!")
        # end if
    # end remove_collector

    # Add a collector
    def add_collector(self, collector):
        """
        Add a collector
        :param collector: A CollectorConfig object to be added
        """
        if collector not in self._repo_collectors:
            self._repo_collectors.append(collector)
        # end if
    # end add_collector

    # Add a depot
    def add_depot(self, depot_new):
        """
        Add a depot
        :param depot_new: New depot to be added
        """
        self._repo_depots.append(depot_new)
    # end add_depot

    # Collector contained in the repository?
    def contains_collector(self, collector):
        """
        Collector contained in the repository?
        :param collector:
        :return:
        """
        return collector in self._repo_collectors
    # end contain_collectors

    # Create laboratory
    def create_laboratory(self, lab_name):
        """
        Create laboratory
        :param lab_name: Laboratory name
        :return: New Laboratory object
        """
        # Laboratory directory
        lab_directory = os.path.join("labs", lab_name)
        lab_cgl_directory = os.path.join(lab_directory, ".cognitivelab")

        # If it does not exists
        if not os.path.exists(lab_directory):
            # Create directory
            os.mkdir(lab_directory)
        # end if

        # If no CGL dir in lab directory
        if not os.path.exists(lab_cgl_directory):
            # Create config directory
            os.mkdir(lab_cgl_directory)
        else:
            raise Exception("Laboratory directory already exists ({})".format(lab_cgl_directory))
        # end if

        # Add to repository in the configuration
        self._repo_labs.append(lab_name)

        # Create the laboratory object
        laboratory_new = Laboratory(lab_name=lab_name)

        return laboratory_new
    # end create_laboratory

    # endregion PUBLIC

# end Repository
