# File : config/Config.py
# Description : Class to access and modify the repository configuration
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
import json
from .Repository import Repository
from cognitivelab.repository.schema import RepositorySchema


# Class to access and modify the repository configuration
class Config(object):
    """
    Class to access and modify the repository configuration
    """

    # Constructor
    def __init__(self, repo_directory):
        """
        Constructor
        :param repo_directory: Main directory of the repository
        """
        # Properties
        self._repo_directory = repo_directory
        self._repo = None

        # Check directory
        self._initialized = self._check_directory()
    # end __init__

    # region PROPERTIES

    # Repository directory
    @property
    def repo_directory(self):
        """
        Get repository directory
        :return: Repository directory
        """
        return self._repo_directory
    # end repo_directory

    # Set repository directory
    @repo_directory.setter
    def repo_directory(self, value):
        """
        Set repository directory
        :param value: New repository directory
        """
        self._repo_directory = value
    # end repo_directory

    # Repository object
    @property
    def repo(self):
        """
        Repository object
        :return: Repository object
        """
        if not self._initialized:
            raise Exception("ERROR: repository not initialized")
        # end if
        return self._repo
    # end repo

    # Repository initialized ?
    @property
    def initialized(self):
        """
        Repository initialized ?
        :return:
        """
        return self._initialized
    # end initialized

    # endregion PROPERTIES

    # region PUBLIC

    # Initialize the repository directory
    def init_repo(self, repo_name):
        """
        Initialize the repository directory
        :param repo_name: Repository name
        :return: The Repository object created with the configuration
        """
        # .cognitivelab base directory path
        cglab_base = os.path.join(self._repo_directory, ".cognitivelab")

        # Create .cognitivelab directory if does not exists
        if not os.path.exists(cglab_base):
            os.mkdir(cglab_base)
        # end if

        # New repository configuration
        self._repo = Repository(
            repo_name=repo_name
        )

        # Save the initialized configuration
        self.save_config()

        # Initialized
        self._initialized = True
    # end init_repo

    # Load the configuration
    def load_config(self):
        """
        Load the configuration
        """
        # Repository schema
        repo_schema = RepositorySchema()

        # Load
        with open(self._repo_json_file(), 'r') as f:
            self._repo = repo_schema.load(json.load(f))
        # end with

        # Initialized
        self._initialized = True
    # end load

    # Save configuration in the JSON file
    def save_config(self):
        """
        Save configuration to the JSON file
        :return: The Repository object
        """
        # Repository schema
        repo_schema = RepositorySchema()

        # Update modification date
        self._repo.update_modification_date()

        # Save
        with open(self._repo_json_file(), 'w') as f:
            json.dump(repo_schema.dump(self._repo), f)
        # end with
    # end save_config

    # endregion PUBLIC

    # region PRIVATE

    # Get JSON repository file
    def _repo_json_file(self):
        """
        Get JSON repository file
        :return:
        """
        return os.path.join(self._repo_directory, ".cognitivelab", "repo.json")
    # end _repo_json_file

    # Check directory
    def _check_directory(self):
        """
        Check directory
        :return: True if directory initialized, False otherwise
        """
        if not os.path.exists(os.path.join(self._repo_directory, ".cognitivelab")) or \
            not os.path.exists(os.path.join(self._repo_directory, ".cognitivelab", "repo.json")):
            return False
        # end if
    # end _check_directory

    # endregion PRIVATE

# end Config
