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
from cognitivelab.repository import collector_factory
from cognitivelab.repository import Config
from .cli_messages import Error_Messages


# Directories to create in init phase
COGNITIVELAB_REPO_MAIN_DIR = '.cognitivelab'
COGNITIVELAB_REPO_DIRS = [
    'data',
    'datasets',
    'labs',
    'models'
]


@click.group('main', chain=True)
@click.pass_context
def main(ctx):
    """
    Manage and analyse outputs of machine learning experiments
    :param ctx: Context
    """
    # Create config object and add to context
    ctx.obj = Config(repo_directory=".")
# end main


@main.command('init')
@click.argument('repo_name')
@click.pass_obj
def init(repo_config, repo_name):
    """
    Init the current directory as a CognitiveLab project directory.
    :param repo_config: Repository configuration
    :param repo_name: Repository name for initialisation
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
        repo_config.init_repo(repo_name=repo_name)
    # end if
# end help


# Command to add a collector for experiments output
@main.command("collector")
@click.argument("action")
@click.argument("collector_type", required=False, default="")
@click.argument("connection_string", required=False, default="")
@click.pass_obj
def collector_command(repo_config, action, collector_type, connection_string):
    """
    Add a collector to the project
    :param repo_config: Repository configuration
    :param action: Action to perform (add, remove)
    :param collector_type: Type of collector ('file', 'mongodb', etc)
    :param connection_string: Connection information or path
    """
    # Load the repository configuration
    try:
        repo_config.load_config()
    except FileNotFoundError:
        click.echo(Error_Messages['REPO_NOT_INITIALIZED'])
        return
    # end try

    # Action
    if action == 'add':
        # Create a new collector that to check
        # that information are correct
        try:
            collector_new = collector_factory.get_collector(
                collector_type,
                connection_string
            )
        except (KeyError, ValueError, Exception) as e:
            click.echo(Error_Messages['CANNOT_GET_COLLECTOR'].format(connection_string, e))
            exit(1)
        # end try

        # Add new collector
        if repo_config.repo.contains_collector(collector_new):
            click.echo(Error_Messages['REPO_ALREADY_CONTAINS_COL'])
            exit(1)
        else:
            repo_config.repo.add_collector(collector_new)
        # end if

        # Save configuration
        repo_config.save_config()
    # Test a collector (connection or path exists)
    elif action == 'test':
        # Go through all collectors
        for collector in repo_config.repo.repo_collectors:
            # Validate
            try:
                # Open and close to test
                collector.open()
                collector.close()
            except Exception as e:
                click.echo(Error_Messages['VALIDATE_COL_FAILED'].format(e))
            finally:
                click.echo("Collector {}:{} validated successfully!".format(
                    collector.collector_type,
                    collector.collector_connection_string
                ))
            # end try
        # end for
    # List of collectors
    elif action == 'list':
        # Go through all collectors
        for collector in repo_config.repo.repo_collectors:
            click.echo("Collector type {} with connection {}".format(
                collector.collector_type,
                collector.collector_connection_string
            ))
    elif action == 'remove':
        # Remove collector
        try:
            repo_config.repo.remove_collector(collector_type, connection_string)
        except Exception as e:
            click.echo(Error_Messages['ERROR_REMOVING_COL'].format(e))
            exit(1)
        # end try

        # Save configuration
        repo_config.save_config()
    elif action == 'sync':
        pass
    elif action == 'update':
        pass
    else:
        click.echo(Error_Messages['UNKNOWN_COL_ACTION'].format(action))
        exit(1)
    # end if
# end add_collector


# Command to manage various labs in the repository
@main.command("labs")
@click.argument("action")
@click.argument("lab_name")
@click.pass_obj
def labs_command(repo_config, action, lab_name):
    """
    Command o
    :param repo_config: Repository configuration object
    :param action: labs action to execute
    :param lab_name: Laboratory name
    """
    # Load the repository configuration
    try:
        repo_config.load_config()
    except FileNotFoundError:
        click.echo(Error_Messages['REPO_NOT_INITIALIZED'])
        return
    # end try

    # Create a laboratory
    if action == 'create':
        # Create laboratory
        try:
            laboratory_new = repo_config.repo.create_laboratory(lab_name)
        except Exception as e:
            click.echo("Cannot create laboratory: {}".format(e))
            exit(1)
        # end try

        # Print success
        click.echo("Laboratory created in {}".format(laboratory_new.lab_directory))
    # end if
# end labs_command


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
# end main_license


# Main
if __name__ == '__main__':
    main()
# end if
