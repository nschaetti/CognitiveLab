
# Imports
import setuptools
import sys
from setuptools import setup


#
try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip
except:
    exit_msg = (
        "pipenv is required to package CognitiveLab. Please install pipenv and try again"
    )
    sys.exit(exit_msg)
# end try

# Package Version
VERSION = "0.1.0"  # PEP-440

# Package name
NAME = "CognitiveLab"

# Package description
DESCRIPTION = "The fastest way to save and analyse Machine Learning experiments in Python"

# Package long description
LONG_DESCRIPTION = (
    "CognitiveLab's open-source framework is the easiest way "
    "for ML/AI researchers to save and analyse the outputs of "
    "experiments, and display conclusions in only a few hours! "
    "Pure Python. Open Source"
)

# Get requirements
pipfile = Project(chdir=False).parsed_pipfile
packages = pipfile["packages"].copy()
requirements = convert_deps_to_pip(packages, r=False)

# Setup
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/nschaetti/CognitiveLab',
    author='nschaetti',
    author_email='nils.schaetti@unige.ch',
    python_requires=">=3.6",
    license='GPL v3',
    packages=setuptools.find_packages(exclude=['tests', 'tests.']),
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True,
    entry_points={"console_scripts": ["cognitivelab = cognitivelab.cli:main"]}
)
