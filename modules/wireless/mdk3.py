#!/usr/bin/env python
#####################################
# Installation module for mdk3
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Chris Anony (vvalien)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update mdk3, a tool for wireless attacks"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/soxrok2212/mdk3-master" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="mdk3"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""cd {INSTALL_LOCATION},./configure,make,make install""
