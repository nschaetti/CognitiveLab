#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : cli_messages.py
# Description : Command line messages and errors
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 03.11.2020 12:26:00
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

# Error messages
Error_Messages = {
    'REPO_NOT_INITIALIZED': "Error: cannot find repository configuration, is this repository initialized?",
    'CANNOT_GET_COLLECTOR': "Error: cannot get collector with connection string \"{}\"",
    'REPO_ALREADY_CONTAINS_COL': "Error: repository already contains a collector with the same remote destination",
    'VALIDATE_COL_FAILED': "Error: validating collector failed ({})",
    'ERROR_REMOVING_COL': "Error removing collector: {}",
    'UNKNOWN_COL_ACTION': "ERROR: unknown collector action: {}",
    'UNKNOWN_LABS_ACTION': "ERROR: unknown labs actions: {}",
    'LAB_ALREADY_EXISTS': "Laboratory directory already exists ({})"
}

