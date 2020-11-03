#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : config/objects/schema/RepositorySchema.py
# Description : Schema for a repository in the configuration
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
from cognitivelab.config.objects import Repository
from .CollectorSchema import CollectorSchema


# Schema for a repository in the configuration
class RepositorySchema(Schema):
    """
    Schema for a repository in the configuration
    """

    # region FIELDS

    # Repository name
    repo_name = fields.Str(
        required=True,
        allow_none=False
    )

    # Repository collectors
    repo_collectors = fields.List(
        fields.Nested(
            CollectorSchema
        ),
        required=True,
        allow_none=False
    )

    # endregion FIELDS

    # region PRIVATE

    # Create Repository object
    @post_load
    def _create_repository(self, data, **kwargs):
        """
        Create Collector object
        :param data:
        :param kwargs:
        :return:
        """
        return Repository(**data)
    # end _create_repository

# end RepositorySchema
