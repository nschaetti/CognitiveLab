#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : config/objects/schema/CollectorSchema.py
# Description : Schema for a collector in the configuration
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
from marshmallow import Schema, fields, post_load, validate
from cognitivelab.repository.CollectorFactory import collector_factory
from cognitivelab.repository.Collector import Collector


# Schema for a collector in the configuration
class CollectorSchema(Schema):
    """
    Schema for a collector in the configuration
    """

    # region FIELDS

    # Collector type
    collector_type = fields.Str(
        required=True,
        allow_none=False,
        validate=validate.OneOf(collector_factory.collector_types())
    )

    # Collector connection string
    collector_connection_string = fields.Str(
        required=True,
        allow_none=False
    )

    # Collector creation date
    collector_creation_date = fields.DateTime(
        required=True,
        allow_none=False
    )

    # Collector last write date
    collector_last_write_date = fields.DateTime(
        required=False,
        allow_none=True
    )

    # endregion FIELDS

    # region PRIVATE

    # Create Collector object
    @post_load
    def _create_collector(self, data, **kwargs):
        """
        Create Collector object
        :param data:
        :param kwargs:
        :return:
        """
        return Collector(**data)
    # end _create_collector

    # endregion PRIVATE

# end CollectorSchema
