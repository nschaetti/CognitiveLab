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
from cognitivelab.collector import collector_factory
from cognitivelab.config import Config
from cognitivelab.config.objects import Collector as CollectorConfig


# Directories to create in init phase
COGNITIVELAB_REPO_MAIN_DIR = '.cognitivelab'
COGNITIVELAB_REPO_DIRS = [
    'data',
    'datasets',
    'lab',
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
@click.argument('repo_name')
def init(repo_name):
    """
    Init the current directory as a CognitiveLab project directory.
    """
    # Check that there is no .cognitivelabs directory
    if os.path.exists(COGNITIVELAB_REPO_MAIN_DIR):
        click.echo('Repository already initialised!')
    else:
        # Prompt
        click.echo("Initializing directory for new lab {}".format(repo_name))
        click.echo("Creating CognitiveLab repository subdirectories:")

        # Create main dir
        os.mkdir(COGNITIVELAB_REPO_MAIN_DIR)

        # For each directory to create
        for project_dir in COGNITIVELAB_REPO_DIRS:
            if os.path.exists(project_dir):
                click.echo("\t- Warning: directory {} already exists!".format(project_dir))
            else:
                os.mkdir(project_dir)
                click.echo("\t- Created directory {}".format(project_dir))
            # end if
        # end for

        # Initialize repository config
        repo_config = Config(repo_directory=".")
        repo_config.init_repo(repo_name=repo_name)
    # end if
# end help


# Command to add a collector for experiments output
@main.command("collector")
@click.argument("collector_type")
@click.argument("action")
@click.argument("destination")
def collector(collector_type, action, destination):
    """
    Add a collector to the project
    :param collector_type: Type of collector (local, distant)
    :param action: Action to perform (add, remove)
    :param destination: Destination of the collector
    """
    # Load the repository configuration
    repo_config = Config(repo_directory=".")
    repo_config.load_config()

    # Action
    if action == 'add':
        # Create a new collector that to check
        # that information are correct
        collector_new = collector_factory.get_collector(
            collector_type,
            destination
        )

        # Validate that the collector
        # is working
        collector_new.validate()

        # Add new collector
        repo_config.repo.add_collector(
            CollectorConfig(
                collector_type=collector_type,
                collector_destination=destination
            )
        )

        # Save configuration
        repo_config.save_config()
    elif action == 'remove':
        pass
    elif action == 'sync':
        pass
    elif action == 'update':
        pass
    else:
        click.echo("ERROR: unknown collector action: {}".format(action))
    # end if
# end add_collector


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
