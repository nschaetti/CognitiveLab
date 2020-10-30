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
import os
import click


# Directories to create in init phase
COGNITIVELAB_PROJECT_MAIN_DIR = '.cognitivelab'
COGNITIVELAB_PROJECT_DIRS = [
    'data',
    'datasets',
    'lab',
    'outputs',
    'tests',
    'models'
]


@click.group('main')
def main():
    """
    Manage and analyse outputs of machine learning experiments
    """
    pass
# end main

@main.command('init')
@click.argument('lab_name')
def init(lab_name):
    """
    Init the current directory as a CognitiveLab project directory.
    """
    # Check that thereis not .cognitivelabs presents
    if os.path.exists(COGNITIVELAB_PROJECT_MAIN_DIR):
        click.echo('Directory already initialised!')
    else:
        # Prompt
        click.echo("Initialising directory for new lab {}".format(lab_name))
        click.echo("Creating CognitiveLab project subdirectories:")

        # Create main dir
        os.mkdir(COGNITIVELAB_PROJECT_MAIN_DIR)

        # For each directory to create
        for project_dir in COGNITIVELAB_PROJECT_DIRS:
            if os.path.exists(project_dir):
                click.echo("\t- Warning: directory {} already exists!".format(project_dir))
            else:
                os.mkdir(project_dir)
                click.echo("\t- Created directory {}".format(project_dir))
            # end if
        # end for
    # end if
# end help


@main.command("version")
def main_version():
    """
    Print CognitiveLab version number.
    """
    click.echo("Version!")
# end main_version


@main.command("license")
def main_license():
    """
    Print CognitiveLab license
    :return:
    """

# Main
if __name__ == '__main__':
    main()
# end if
