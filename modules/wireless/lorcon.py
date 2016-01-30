#!/usr/bin/env python
#####################################
# Installation module for lorcon drivers
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Chris Anony (vvalien)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update lorcon/PyLorcon2/ruby-lorcon, wireless injection drivers!"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://code.google.com/p/lorcon/" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="lorcon"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libnl-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""cd {INSTALL_LOCATION},./configure,make,make install,cp /usr/local/lib/liborcon* /usr/lib/,cd {INSTALL_LOCATION}pylorcon2,python setup.py install,cd {INSTALL_LOCATION}ruby-lorcon,ruby extconf.rb,make,make install""
