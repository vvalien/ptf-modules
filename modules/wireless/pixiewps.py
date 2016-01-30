#!/usr/bin/env python
#####################################
# Installation module for pixiewps
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Chris Anony (vvalien)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update pixiewps, the offline wps attack tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/wiire/pixiewps" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pixiewps"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libssl-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""cd {INSTALL_LOCATION}src,make,make install""
