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
import importlib


# Load experiment class from target module
def load_xp_class(module_path, xp_class_name, package='.'):
    """
    Load experiment class from target module
    :param module_path: Path to module
    :param xp_class_name: Experiment class
    :param package:
    """
    # Load module
    xp_module = importlib.import_module(module_path, package)

    # Get class
    xp_class = getattr(xp_module, xp_class_name)

    # Create object
    xp_obj = xp_class()

    return xp_obj
# end launch_script
