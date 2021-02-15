#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : debug_tools.py
# Description : Debug tools for Cognitive Lab
# Author : Nils Schaetti <n.schaetti@gmail.com>
# Date : 12.02.2020 14:56:00
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


# Print message
def echo(message, level=0):
    """
    Print message
    :param message: Message
    :param level: Debug level
    """
    print("[{}]: {}".format(message, level))
# end print
