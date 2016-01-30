#!/usr/bin/env python
#####################################
# Installation module for reaver-pixiewps
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Chris Anony (vvalien)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update reaver, this is the modified t6x version for pixiewps"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/t6x/reaver-wps-fork-t6x" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="reaver-pixiewps"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="build-essential libpcap-dev sqlite3 libsqlite3-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""cd {INSTALL_LOCATION}src,./configure,make,make install,exit""
