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
import datetime


# Manage a laboratory and its configuration
class Laboratory(object):
    """
    Manage a laboratory and its configuration
    """

    # Constructor
    def __init__(self, lab_name, lab_creation_date=None, lab_modification_date=None):
        """
        Constructor
        :param lab_name: Laboratory name
        """
        # Properties
        self._lab_name = lab_name

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

    # endregion PROPERTIES

# end Laboratory