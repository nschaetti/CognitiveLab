# File : config/__init__.py
# Description : Repository configuration package init file
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
from .Config import Config
from . import Repository
from . import Collector
from . import CollectorFactory
from .CollectorFactory import collector_factory
from . import Laboratory
from . import MongoDBCollector
from .RemoteDepot import RemoteDepot
from . import schema

# ALL
__all__ = ['Config', 'RemoteDepot', 'Repository', 'Collector', 'CollectorFactory', 'MongoDBCollector',
           'collector_factory', 'Laboratory', 'schema']
