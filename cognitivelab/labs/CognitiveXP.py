#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : cli.py
# Description : Command line handler for CognitiveLab
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 30.10.2020 15:55:00
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

def check_empty(attr):
   def check_method(function):
     def wrapped(cls, **kwargs):
       if kwargs.get(attr) is None:
         raise Exception('{item} cannot be empty'.format(item=attr))
       return function(cls, **kwargs)
     return wrapped
   return check_method


# Experiment parameter (decorator)
def xp_param(param_name, param_type, param_default, param_required=False):
    """
    Experiment parameter (decorator)
    :param param_name:
    :param param_type:
    :param param_default:
    :param param_required:
    :return:
    """
    def func(function):
        def wrapper(cls, **kwargs):
            xp_obj = function(cls, **kwargs)
            xp_obj.add_param(param_name, param_type, param_default)
            return xp_obj
        # end wrapper
        return wrapper
    # end func
    return func
# end xp_param


# Experiment parameter (decorator class)
def xpc_param(param_name, param_type, param_default, param_required=False):
    """
    Experiment parameter (decorator class)
    :param param_name:
    :param param_type:
    :return:
    """
    def func(cls):
        class ParamXP(cls):
            def __init__(self, *args, param_name=param_default, **kwargs):
                self.add_xp_param(param_name, param_type, param_required)
                super(ParamXP, self).__init__(*args, **kwargs)
            # end __init__
        # end ParamXP
    # end func
    return func
# end xpc_param


# Cognitive Lab experiment class
class CognitiveXP(object):
    """
    Cognitive Lab experiment class
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, context, dataset_class_name):
        """
        Constructor
        :param context: Cognitive Lab context
        """
        # Properties
        self._context = context
    # end __init__

    # endregion CONSTRUCTORS

    # region PUBLIC

    # Init XP
    def init(self):
        """
        Init XP
        :return:
        """
        pass
    # end init

    # Create dataset
    def create_dataset(self):
        """
        Create dataset
        :return:
        """
        pass
    # end create_dataset

    # Run the XP
    def run(self):
        """
        Run the XP
        """
        pass
    # end run

    # Close XP
    def close(self):
        """
        Close XP
        :return:
        """
        pass
    # end close

    # endregion PUBLIC

# end CognitiveXP