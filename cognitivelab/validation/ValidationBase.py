#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : CrossValidation.py
# Description : K-Fold cross validation
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 10.10.2020 15:30
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
from torch.utils.data.dataset import Dataset


# Base class for validation method
class ValidationBase(Dataset):
    """
    Base class for validation method
    """

    # Constructor
    def __init__(self, root_dataset):
        """
        Constructor
        :param root_dataset: Base dataset to validate
        """
        # Properties
        self._root_dataset = root_dataset
    # end __init__

    # region DECORATORS

    # endregion DECORATORS

    # region PUBLIC

    # Serialize the validation instance
    def serialize(self, output_file):
        """
        Serialize the validation instance
        :param output_file: Output file for serialization
        """
        pass
    # end serialize

    # endregion PUBLIC

    # region STATIC

    # Deserialize the validation instance
    def deserialize(self, input_file):
        """
        Deserialize the validation instance
        :param input_file: Serialized file
        :return: Deserialized ValidationBase object
        """
        pass
    # end deserialize

    # endregion STATIC

# end ValidationBase
