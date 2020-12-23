#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : repository/Laboratory.py
# Description : Manage a laboratory and its configuration
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
import configparser


# Manage a laboratory and its configuration
class Laboratory(object):
    """
    Manage a laboratory and its configuration
    """

    # Constructor
    def __init__(self, lab_name, lab_directory, lab_creation_date=None, lab_modification_date=None):
        """
        Constructor
        :param lab_name: Laboratory name
        :param lab_directory: Laboratory directory
        :param lab_creation_date: Date and time of the creation of the laboratory
        :param lab_modification_date: Date and time of the last modification of the laboratory
        """
        # Properties
        self._lab_name = lab_name
        self._lab_directory = lab_directory

        # Dates
        self._lab_creation_date = datetime.datetime.now() if lab_creation_date is None else lab_creation_date
        self._lab_modification_date = datetime.datetime.now() if lab_modification_date is None else lab_modification_date
    # end __init__

    # region PROPERTIES

    # Get lab name
    @property
    def lab_name(self):
        """
        Get lab name
        :return: Laboratory name
        """
        return self._lab_name
    # end lab_name

    # Set lab name
    @lab_name.setter
    def lab_name(self, value):
        """
        Set lab name
        """
        self._lab_name = value
    # end lab_name

    # Get lab directory
    @property
    def lab_directory(self):
        """
        Get lab directory
        :return: Lab directory
        """
        return self._lab_directory
    # end lab_directory

    # Set lab directory
    @lab_directory.setter
    def lab_directory(self, value):
        """
        Set lab directory
        :param value: New path for the lab
        """
        self._lab_directory = value
    # end lab_directory

    # endregion PROPERTIES

    # region PUBLIC

    # Create an empty configuration file
    def create_config_file(self):
        """
        Create an empty configuration file
        """
        # Config parser
        default_config = configparser.ConfigParser()

        # Default section
        default_config['data'] = {}
        default_config['evaluation'] = {}

        # Write file
        with open(os.path.join(self._lab_directory, ".cognitivelab", "config"), "w") as c_file:
            default_config.write(c_file)
        # end with
    # end create_config_file

    # endregion PUBLIC

    # region STATIC

    # Initialise a new laboratory
    @staticmethod
    def initialize(lab_name, cl_dir, repo):
        """
        Initialize a new laboratory
        :param lab_name: New laboratory name
        :param cl_dir: CognitiveLab root directory
        :param repo: Repository object to be updated
        :return: Laboratory object
        """
        # Laboratory directory
        lab_directory = os.path.join(cl_dir, lab_name)
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

        # Create the laboratory object
        laboratory_new = Laboratory(lab_name=lab_name, lab_directory=lab_directory)

        return laboratory_new

    # endregion STATIC

# end Laboratory