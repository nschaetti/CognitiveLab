#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : RemoteDepot.py
# Description : Class to handle remote CognitiveLab depots
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 10.11.2020 16:00:00
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

# Imports
import datetime
import requests
from tinydb import TinyDB, Query


# Class to handle remote CognitiveLab depots
class RemoteDepot(object):
    """
    Class to handle remote CognitiveLab depots
    """

    # Constructor
    def __init__(self, remote_location, locale_db, last_update_date=None, dataset_subdir='data'):
        """
        Constructor
        :param remote_location: Remote location URL
        :param locale_db: Locale version of the index
        :param last_update_date: Last time the depot was updated
        """
        # Properties
        self._remote_location = remote_location
        self._locale_db = locale_db
        self._dataset_subdir = dataset_subdir

        # Last update date
        if last_update_date is None:
            self._last_update_date = datetime.datetime.now()
        else:
            self._last_update_date = last_update_date
        # end if

        # Open database
        self._db = self._open_database()

        # Tables
        self._databases_table = self._db.table('databases')
    # end __init__

    # region PROPERTIES

    # Remote location
    @property
    def remote_location(self):
        """
        Remote location
        """
        return self._remote_location
    # end remote_location

    # Locale database file
    @property
    def locale_db(self):
        """
        Locale database file
        :return: Path to DB file
        """
        return self._locale_db
    # end locale_db

    # Last update date
    @property
    def last_update_date(self):
        """
        Last update date
        :return: Last update date
        """
        return self._last_update_date
    # end last_update_date

    # Get dataset depot
    @property
    def dataset_depot(self):
        """
        Get dataset depot
        :return: List of references
        """
        return self._dataset_depot
    # end dataset_depot

    # endregion PROPERTIES

    # region PUBLIC

    # Clear the depot
    def clear(self):
        """
        Clear the depot
        """
        self._dataset_depot = dict()
    # end clear

    # Upgrade all packages in the depot
    def upgrade(self):
        """
        Upgrade all packages in the depot
        :return:
        """
        pass
    # end upgrade

    # Update the index
    def update(self):
        """
        Update the index
        :return:
        """
        # Remote index
        separator_url = "" if self._remote_location[-1] == "/" else "/"
        remote_index = self._remote_location + separator_url + "index"

        # Get index file
        resp = requests.get(remote_index)

        # Save the content in the filename
        with open(self._locale_db, 'wb') as f_db:
            f_db.write(resp.content)
        # end with
    # end update

    # Is a dataset in the depot?
    def dataset_in(self, dataset_name, dataset_version='all'):
        """
        Is a dataset in the depot?
        :param dataset_name: Dataset name
        :param dataset_version: Dataset version
        :return: True/False
        """
        """if dataset_version != 'all':
            return (dataset_name, dataset_version) in self._dataset_depot.keys()
        else:
            for d_name, _ in self._dataset_depot.keys():
                if dataset_name == d_name:
                    return True
                # end if
            # end for
            return False
        # end for"""
        pass
    # end dataset_in

    # Add a dataset to the depot
    def add_dataset(self, dataset_name, dataset_version, remote_file):
        """
        Add a dataset to the depot
        :param dataset_name: Dataset name
        :param dataset_version: Dataset version
        :param remote_file: Filename on the remote host
        """
        # self._dataset_depot[(dataset_name, dataset_version)] = remote_file
        self._databases_table.insert({
            'name': dataset_name,
            'version': dataset_version,
            'last_update': datetime.datetime.now(),
            'remote_file': remote_file
        })
    # end add_dataset

    # endregion PUBLIC

    # region PRIVATE

    # Open the TinyDB database
    def _open_database(self):
        """
        Open the TinyDB database
        """
        return TinyDB(self._locale_db)
    # endregion PRIVATE

# end RemoteDepot
