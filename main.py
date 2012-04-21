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

message ('============================')
message ('BEGIN REMOVING MISC PACKAGES')
message ('NOTE: The screen output is suppressed due to excessive volume.')

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

# Remove Firefox
purge_packages ('firefox firefox-l10n-en-us')

# Remove packages from the cli-mono section
# The cli_mono.txt list was compiled by selecting all cli-mon packages in Synaptic,
# marking to install them, and going to File -> Save Markings As
message ('PURGING cli-mono packages')
purge_packages_file (dir_develop + "/remove-misc/cli_mono.txt")

# Remove Thunderbird (email suite)
#os.system('apt-get purge -y thunderbird thunderbird-l10n-en-us')
purge_packages ('thunderbird thunderbird-l10n-en-us')

# Remove XChat
#os.system('apt-get purge -y xchat-common xchat')
purge_packages ('xchat-common xchat')

# Remove GhostScript packages

# Remove GIMP
#os.system('apt-get purge -y gimp gimp-data libgimp2.0')
purge_packages ('gimp gimp-data libgimp2.0')
#os.system('apt-get purge -y cups-driver-gutenprint libgutenprint2')
purge_packages ('cups-driver-gutenprint libgutenprint2')
#os.system('apt-get purge -y libgtk2-perl libgnome2-canvas-perl libgnome2-perl')
purge_packages ('libgtk2-perl libgnome2-canvas-perl libgnome2-perl')

# Remove Giver
#os.system('apt-get purge -y giver')
purge_packages ('giver')

# Remove Samba
#os.system('apt-get purge -y samba samba-common samba-common-bin')
purge_packages ('samba samba-common samba-common-bin')

# Remove Telepathy
#os.system('apt-get purge -y libtelepathy-glib0 vino')
purge_packages ('libtelepathy-glib0 vino')
#os.system('apt-get purge -y telepathy-mission-control-5 telepathy-gabble telepathy-salut')
purge_packages ('telepathy-mission-control-5 telepathy-gabble telepathy-salut')

# Remove VLC Media Player
#os.system('apt-get purge -y vlc vlc-data vlc-nox vlc-plugin-notify vlc-plugin-pulse')
purge_packages ('vlc vlc-data vlc-nox vlc-plugin-notify vlc-plugin-pulse')
#os.system('apt-get purge -y libvlc5 libvlccore4')
purge_packages ('libvlc5 libvlccore4')

# Remove selected packages from the editors section
#os.system('apt-get purge -y nano vim-common vim-tiny')
purge_packages ('nano vim-common vim-tiny')

# Remove selected packages from the font section
#os.system('apt-get purge -y ttf-bengali-fonts')
purge_packages ('ttf-bengali-fonts')
#os.system('apt-get purge -y ttf-gujarati-fonts')
purge_packages ('ttf-gujarati-fonts')
#os.system('apt-get purge -y ttf-punjabi-fonts')
purge_packages ('ttf-punjabi-fonts')
#os.system('apt-get purge -y ttf-sazanami-gothic')
purge_packages ('ttf-sazanami-gothic')
#os.system('apt-get purge -y ttf-sazanami-mincho')
purge_packages ('ttf-sazanami-mincho')
#os.system('apt-get purge -y ttf-tamil-fonts')
purge_packages ('ttf-tamil-fonts')
#os.system('apt-get purge -y ttf-telugu-fonts')
purge_packages ('ttf-telugu-fonts')

# Remove packages from httpd section
#os.system('apt-get purge -y apache2.2-bin libapache2-mod-dnssd')
purge_packages ('apache2.2-bin libapache2-mod-dnssd')

# Remove selected packages (cpp) from the interpreter section
#os.system('apt-get purge -y cpp-4.3 gcc-4.3')
purge_packages ('cpp-4.3 gcc-4.3')

# Remove packages from lisp section
#os.system('apt-get purge -y guile-1.8-libs')
purge_packages ('guile-1.8-libs')

# Remove selected packages from the mail section
#os.system('apt-get purge -y exim4-config procmail')
purge_packages ('exim4-config procmail')

# Remove selected packages from the math section
#os.system('apt-get purge -y dc')
purge_packages ('dc')

# Remove packages from ruby section and selected other Ruby packages
#os.system('apt-get purge -y libdpkg-ruby1.8 libgettext-ruby1.8 liblocale-ruby1.8')
purge_packages ('libdpkg-ruby1.8 libgettext-ruby1.8 liblocale-ruby1.8')
#os.system('apt-get purge -y libhttpclient-ruby1.8 libxml-parser-ruby1.8')
purge_packages ('libhttpclient-ruby1.8 libxml-parser-ruby1.8')
#os.system('apt-get purge -y ruby ruby-xmlparser ruby1.8') 
purge_packages ('ruby ruby-xmlparser ruby1.8') 
#os.system('apt-get purge -y libruby libruby1.8') 
purge_packages ('libruby libruby1.8') 

# Remove selected Mint packages (search for Mint)
#os.system('apt-get purge -y debian-system-adjustments') 
purge_packages ('debian-system-adjustments') 
#os.system('apt-get purge -y grub2-theme-mint') 
purge_packages ('grub2-theme-mint') 
#os.system('apt-get purge -y mint-stylish-addon')
purge_packages ('mint-stylish-addon')
#os.system('apt-get purge -y mintinstall-icons')
purge_packages ('mintinstall-icons')

# Remove Python 3.2
#os.system('apt-get purge -y python3.2 python3 python3-apt wajig')
purge_packages ('python3.2 python3 python3-apt wajig')
#os.system('apt-get purge -y python3.2-minimal python3-minimal')
purge_packages ('python3.2-minimal python3-minimal')

# Remove selected GCC packages
#os.system('apt-get purge -y gcc g++ build-essential dkms ndiswrapper-dkms')
purge_packages ('gcc g++ build-essential dkms ndiswrapper-dkms')
#os.system('apt-get purge -y gcc-4.3-base')
purge_packages ('gcc-4.3-base')
#os.system('apt-get purge -y gcc-4.6 g++ g++-4.6  libstdc++6-4.6-dev')
purge_packages ('gcc-4.6 g++ g++-4.6  libstdc++6-4.6-dev')

# Remove selected Ghostscript packages
#os.system('apt-get purge -y ghostscript-cups ghostscript-x gs gs-common')
purge_packages ('ghostscript-cups ghostscript-x gs gs-common')

# Removing selected packages from the sound section of Synaptic
#os.system('apt-get purge -y espeak espeak-data libespeak1') #eSpeak
purge_packages ('espeak espeak-data libespeak1') #eSpeak

# Removing selected packages from the text section of Synaptic
#os.system('apt-get purge -y liblouis-data') #Liblouis
purge_packages ('liblouis-data') #Liblouis


# Removing selected packages from the web section of Synaptic
#os.system('apt-get purge -y w3m')
purge_packages ('w3m')

# Removing g++-4.4 and ibstdc++6-4.4-dev
#os.system('apt-get purge -y g++-4.4 libstdc++6-4.4-dev')
purge_packages ('g++-4.4 libstdc++6-4.4-dev')

# Removing libflite1 gstreamer0.10-plugins-bad libgstfarsight0.10-0
#os.system('apt-get purge -y libflite1 gstreamer0.10-plugins-bad libgstfarsight0.10-0')
purge_packages ('libflite1 gstreamer0.10-plugins-bad libgstfarsight0.10-0')

# Removing packages listed when typing "apt-get autoremove"
purge_packages ('libcurl3-nss liboauth0 libgdata13')
purge_packages ('libgail-3-0 libwebkitgtk-3.0-0 libgoa-1.0-0')
purge_packages ('libgoa-1.0-common')
purge_packages ('libicu48 libjavascriptcoregtk-3.0-0')
purge_packages ('librest-0.7-0')
purge_packages ('libwebkitgtk-3.0-common')



# The following file should be deleted: /home/(username)/.linuxmint/mintMenu/apt.cache
file_to_delete = dir_user + "/.linuxmint/mintMenu/apt.cache"
if (os.path.exists(file_to_delete)):
    os.remove (file_to_delete)

message ('FINISHED REMOVING MISC PACKAGES')
message ('===============================')


