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

# ==========
# No Compiz packages remain
# ==========
message ('Removing Evince packages')
purge_packages ('evince evince-common')
purge_packages ('gir1.2-evince-3.0 gir1.2-sushi-1.0')
purge_packages ('libevince2 libevince3-3 libsushi-1.0-0')
# ==========
message ('Removing Evolution packages')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/evolution.txt")
# ==========
message ('Removing remaining MATE packages')
purge_packages ('libmateconf libmatecorba libmatenotify mate-notification-daemon')
# ==========
message ('Removing Mint-specific MDM packages')
purge_packages ('mint-mdm-themes mate-session-manager')
# ==========
message ('Removing remaining Metacity packages')
purge_packages ('murrine-themes')
# ==========
message ('Removing remaining selected Nautilus packages')
purge_packages ('nautilus gnome-sushi nautilus-open-terminal')

# ==========
message ('Removing extra GNOME media packages')      
purge_packages ('banshee banshee-extension-soundmenu')

message ('Removing Brasero packages')
purge_packages ('brasero brasero-common libbrasero-media3-1')

# Remove GNOME Sound Recorder
purge_packages ('gnome-media')

message ('Removing Totem packages')
purge_packages ('totem totem-common')
purge_packages ('gir1.2-totem-plparser-1.0 gir1.2-totem-1.0')
purge_packages ('gstreamer0.10-pitfdll mint-meta-codecs')
purge_packages ('libtotem-plparser17 libtotem0')

# ==========
# Removing other GNOME packages
# Remove Gmenu (menu editor)
purge_packages ('gnome-menus')
# Remove GNOME Character Map
purge_packages ('gucharmap')
# Remove gthumb (thumbnails)
purge_packages ('gthumb gthumb-data')

# ==========
# Removing packages classified in Synaptic in section "gnome"
purge_packages ('at-spi')
purge_packages ('cups-pk-helper')
purge_packages ('gnome-desktop-data')  
purge_packages ('gnome-desktop3-data libgnome-desktop-3-2 gnome-settings-daemon')    
purge_packages ('gnome-icon-theme-symbolic')
purge_packages ('gnome-media-common libgnome-media0')
purge_packages ('gnome-mime-data libgnomevfs2-common')
purge_packages ('gnome-session-bin')
purge_packages ('gnome-session-common gnome-sushi-common')
purge_packages ('gtk2-engines mint-artwork-debian')
purge_packages ('gtk2-engines-aurora')
purge_packages ('gtk2-engines-candido')
purge_packages ('gtk3-engines-unico')

# Remove Seahorse
purge_packages ('seahorse')

# Remove Tomboy (note taking)
purge_packages ('tomboy')

# Remove Yelp
purge_packages ('gnome-doc-utils yelp')

# Remove Zenity
purge_packages ('zenity')

# Remove GNOME Desktop Environment (universe) and dependants
purge_packages ('mint-x-icons mint-x-theme')

# Remove GNOME Desktop Environment and dependants
# To see the list of installed packages, open Synaptic and go to Sections -> 
# GNOME Desktop Environment and sort by the first column.

purge_packages ('capplets-data')
purge_packages ('gnome-audio')
purge_packages ('gnome-desktop-data')
purge_packages ('gnome-media-common libgnome-media0')
purge_packages ('gnome-session-bin gnome-session-canberra gnome-session-common')
purge_packages ('gnome-settings-daemon')
purge_packages ('gnome-system-tools')
purge_packages ('policykit-1-gnome libpolkit-gtk-1-0')
purge_packages ('mintnanny') # MintNanny      

# GNOME Network Manager
purge_packages ('network-manager network-manager-pptp network-manager-pptp-gnome') 
purge_packages ('libnm-glib-vpn1 libnm-glib2 libnm-glib4 libnm-util1 libnm-util2')

if os.path.exists('/usr/share/icons/gnome/icon-theme.cache'):
    print ('Removing /usr/share/icons/gnome/icon-theme.cache')
    os.remove('/usr/share/icons/gnome/icon-theme.cache')



# List compiled by searching Synaptic Description and Name for "Firefox".
# Keeping gecko-mediaplayer and PCManFM
purge_packages ('firefox firefox-l10n-en-us mint-search-addon mint-stylish-addon')

message ('Removing Pidgin')
purge_packages ('pidgin pidgin-data pidgin-facebookchat libpurple0 libpurple-bin')

# Remove Thunderbird
purge_packages ('thunderbird thunderbird-l10n-en-us')

# Remove XChat
purge_packages ('xchat-common xchat')

# Remove GIMP/Gutenprint
message ('Removing GIMP/Gutenprint')
purge_packages ('gimp gimp-data libgimp2.0')
purge_packages ('cups-driver-gutenprint libgutenprint2 printer-driver-gutenprint')
purge_packages ('libgegl-0.0-0')

# Remove Samba
purge_packages ('samba samba-common samba-common-bin')

# Remove Telepathy
message ('Removing Telepathy')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/telepathy.txt")

# Remove VLC Media Player
#os.system('apt-get purge -y vlc vlc-data vlc-nox vlc-plugin-notify vlc-plugin-pulse')
purge_packages ('vlc vlc-data vlc-nox vlc-plugin-notify vlc-plugin-pulse')
#os.system('apt-get purge -y libvlc5 libvlccore4')
purge_packages ('libvlc5 libvlccore4')

# Remove selected packages from the editors section
#os.system('apt-get purge -y nano vim-common vim-tiny')
purge_packages ('nano vim-common vim-tiny')

message ('Removing excess fonts')
purge_packages_file (dir_develop + "/remove-misc/remove-deb/fonts.txt")


message ('FINISHED REMOVING MISC PACKAGES')
message ('===============================')


