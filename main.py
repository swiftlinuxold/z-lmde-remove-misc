#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

def message (string):
    os.system ('echo ' + string)

def purge_packages (packages):
    os.system ('echo PURGING ' + packages)
    os.system ('apt-get purge -qq ' + packages)
    
def purge_packages_file (filename):
    list_with_newlines = open(filename, 'r').read()
    list_with_spaces = list_with_newlines.replace ('\n', ' ')
    os.system ('apt-get purge -qq ' + list_with_spaces)

# Handy commands
# deborphan -n (package name)
# sudo apt-get purge -s (package name): simulation only
# sudo apt-get autoremove (enter N)

message ('============================')
message ('BEGIN REMOVING MISC PACKAGES')
message ('NOTE: The screen output is suppressed due to excessive volume.')

# List compiled by searching Synaptic Description and Name for "Evolution".
message ('Removing Evolution packages')
purge_packages_file (dir_develop + '/remove-misc/remove-deb/evolution.txt')

# List compiled by searching Synaptic Description and Name for "Firefox".
# Keeping gecko-mediaplayer and PCManFM
purge_packages ('firefox firefox-l10n-en-us mint-search-addon mint-stylish-addon')






message ('FINISHED REMOVING MISC PACKAGES')
message ('===============================')


