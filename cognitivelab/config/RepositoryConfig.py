#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : config/RepositoryConfig.py
# Description : Class to load, save and access repository configuration.
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 01.11.2020 23:21:00
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


# Class to load, save and access repository configuration.
class RepositoryConfig(object):
    """
    Class to load, save and access repository configuration.
    """

    # Constructor
    def __init__(self, repo_name, repo_collectors=None):
        """
        Constructor
        :param repo_name: Repository name
        :param repo_collectors: List of CollectorConfig objects
        """
        # Repository name
        self._repo_name = repo_name

        # Repository collectors
        if repo_collectors is None:
            self._repo_collectors = list()
        else:
            self._repo_collectors = repo_collectors
        # end if
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

    # endregion PROPERTIES

    # region PUBLIC

    # Add a collector
    def add_collector(self, collector):
        """
        Add a collector
        :param collector: A CollectorConfig object to be added
        """
        self._repo_collectors.append(collector)
    # end add_collector

    # endregion PUBLIC

# end RepositoryConfig
