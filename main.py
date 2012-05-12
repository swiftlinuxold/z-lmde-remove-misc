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

# PART 1: REMOVING PACKAGES FROM SELECTED SECTIONS + RELATED PACKAGES
# Synaptic -> Preferences -> show Section
# Then sort by Section
# Use Synaptic to search for related packages
# Use 'deborphan' and 'deborphan -n' commands to search for related packages

message ('PART 1: removing packages from the database section')
purge_packages ('unixodbc libodbc1 odbcinst odbcinst1debian2')

message ('PART 1: removing selected packages from the devel section')
purge_packages ('bison libbison-dev')
purge_packages ('flex')
purge_packages ('g++-4.4 libstdc++6-4.4-dev')
purge_packages ('gcc-4.4 cpp-4.4 gcc-4.4')
purge_packages ('libtasn1-3-bin')
      
message ('PART 1: removing selected packages from the editors section')
purge_packages ('nano vim-common vim-tiny')

message ('PART 1: removing selected fonts')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/fonts.txt")

message ('PART 1: removing packages from the games section')
purge_packages ('cowsay fortune-mod fortunes-husse fortunes-min')

message ('PART 1: removing packages from the gnome section')
purge_packages ('at-spi libatspi1.0-0')
purge_packages ('brasero brasero-common libbrasero-media3-1')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/evince.txt")
purge_packages_file (dir_develop + "/remove-misc/remove-deb/evolution.txt")
purge_packages ('gnome-desktop-data')  
purge_packages_file (dir_develop + "/remove-misc/remove-deb/nautilus.txt")
purge_packages ('gnome-icon-theme-symbolic')
purge_packages ('gnome-media gnome-media-common libgnome-media0')
purge_packages ('gnome-menus')
purge_packages ('gnome-mime-data libgnomevfs2-common')
purge_packages ('gnome-session-bin')
purge_packages ('gnome-session-common')
purge_packages ('gthumb gthumb-data')
purge_packages ('gtk2-engines mint-artwork-debian')
purge_packages ('gtk2-engines-aurora')
purge_packages ('gtk2-engines-candido')
purge_packages ('gtk3-engines-unico murrine-themes')
purge_packages ('gucharmap')
purge_packages ('libbonobo2-common libbonobo2-0 libgnome-speech7 libbonoboui2-common')
purge_packages ('libgnome-menu2 libslab0a libgnome-window-settings1 python-gmenu')
purge_packages ('seahorse seahorse-daemon libcryptui0a')
purge_packages ('tomboy')      
purge_packages ('vino')
purge_packages ('zenity zenity-common')

message ('PART 1: removing packages from the graphics section')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/gimp_gutenprint.txt")
purge_packages ('gtk2-engines-pixbuf')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/imagemagick.txt")

message ('PART 1: removing packages from the httpd section')
purge_packages ('apache2.2-bin libapache2-mod-dnssd')

message ('PART 1: removing packages from the interpreters section')
purge_packages ('cpp-4.3')
# Totem is removed here
purge_packages_file (dir_develop + "/remove-misc/remove-deb/gnome-js-common.txt")
purge_packages ('m4')
purge_packages ('tcl tcl8.4 tcl8.5')

message ('PART 1: removing packages from the lisp section')
purge_packages ('guile-1.8-libs')

message ('PART 1: removing packages from the mail section')
purge_packages ('exim4-config procmail')
purge_packages ('thunderbird thunderbird-l10n-en-us')

message ('PART 1: removing packages from the math section')
purge_packages ('dc')

message ('PART 1: removing packages from the misc section')
purge_packages ('grub2-theme-mint')
purge_packages ('libpango1.0-common')

message ('PART 1: removing packages from the net section')
purge_packages ('dnsmasq-base')
purge_packages ('libpurple-bin libpurple0 pidgin pidgin-data pidgin-facebookchat ')
purge_packages ('samba samba-common samba-common-bin')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/telepathy.txt")
purge_packages ('xchat-common xchat')

message ('PART 1: removing packages from the ruby section')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/ruby.txt")

message ('PART 1: removing packages from the sound section')
purge_packages ('banshee banshee-extension-soundmenu')
purge_packages ('espeak espeak-data libespeak1')

message ('PART 1: removing packages from the text section')
purge_packages ('liblouis-data')

message ('PART 1: removing packages from the universe/gnome section')
purge_packages ('mint-x-icons mint-x-theme')

message ('PART 1: removing packages from the video section')
purge_packages ('vlc vlc-data vlc-nox vlc-plugin-notify vlc-plugin-pulse')
purge_packages ('libvlc5 libvlccore4')

message ('PART 1: removing packages from the web section')
purge_packages ('firefox firefox-l10n-en-us mint-search-addon mint-stylish-addon')
purge_packages ('w3m')

message ('PART 1: removing packages from the x11 section')
purge_packages ('gtk2-engines-murrine')
purge_packages ('libdecoration0')
purge_packages ('mate-notification-daemon libmateconf libmatecorba libmatenotify')
purge_packages ('ttf-wqy-microhei')

message ('PART 1: removing packages from the zope section')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/zope.txt")

message ('PART 1: removing packages from the cli-mono section')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/cli_mono.txt")


# PART 2: Description + Name search for a key word, remove selected packages
message ('PART 2: search for Mint, remove selected packages')
purge_packages ('debian-system-adjustments')
purge_packages ('mint-backgrounds-debian')
purge_packages ('mint-mdm-themes')    

message ('PART 2: search for gcc, remove selected packages')
purge_packages ('gcc-4.3-base gcc-4.4-base')

message ('PART 2: search for python3, remove selected packages')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/python3.txt")


if os.path.exists('/usr/share/icons/gnome/icon-theme.cache'):
    print ('Removing /usr/share/icons/gnome/icon-theme.cache')
    os.remove('/usr/share/icons/gnome/icon-theme.cache')

message ('FINISHED REMOVING MISC PACKAGES')
message ('===============================')


