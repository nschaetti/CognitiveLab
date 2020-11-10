#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : RemoteDepotSchema.py
# Description : Schema for remote depot class
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
from marshmallow import Schema, fields, post_load, validate
from cognitivelab.repository.RemoteDepot import RemoteDepot


# Schema for remote depot class
class RemoteDepotSchema(Schema):
    """
    Schema for remote depot class
    """

    # region FIELDS

    # Remote location
    remote_location = fields.Str(validate=validate.URL())

    # Last update date
    last_update_date = fields.DateTime()

    # Dataset depot
    dataset_depot = fields.Dict(
        keys=fields.Tuple(tuple_fields=[fields.Str(), fields.Str()]),
        values=fields.Str()
    )

    # Dataset subdir
    dataset_subdir = fields.Str()

    # endregion FIELDS

    # region PRIVATE

    # Create the RemoteDepot object
    @post_load
    def _create_remote_depot(self, data, **kwargs):
        """
        Create the RemoteDepot object
        :param data: Data
        :param kwargs: Arguments
        """
        return RemoteDepot(**data)
    # end _create_remote_depot

    # endregion PRIVATE

# end RemoteDepotClass
