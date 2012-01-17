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
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

print '======================='
print 'BEGIN REMOVING PACKAGES'

# Remove GIMP
os.system('apt-get remove -y gimp gimp-data')
os.system('apt-get remove -y libgimp2.0')

# Remove LibreOffice Base
os.system('apt-get remove -y libreoffice libreoffice-base libreoffice-report-builder-bin')

# Remove LibreOffice Draw and Impress
os.system('apt-get remove -y libreoffice-draw libreoffice-impress')

# Remove LibreOffice Math
os.system('apt-get remove -y libreoffice-math')

# Remove other LibreOffice packages
os.system('apt-get remove -y libreoffice-emailmerge')
os.system('apt-get remove -y libreoffice-filter-mobiledev')      
os.system('apt-get remove -y libreoffice-gnome')      
os.system('apt-get remove -y libreoffice-gtk')      
os.system('apt-get remove -y libreoffice-java-common')      
os.system('apt-get remove -y libreoffice-report-builder-bin') 
os.system('apt-get remove -y python-uno')

# Remove admin packages
os.system('apt-get remove -y mint-backgrounds-debian mint-backgrounds-katya mint-backgrounds-katya-extra')
os.system('apt-get remove -y mint-stylish-addon')
os.system('apt-get remove -y mintwelcome')

# Remove editors
os.system('apt-get remove -y nano vim-common vim-tiny')

# Remove fonts
os.system('apt-get remove -y ttf-bengali-fonts')
os.system('apt-get remove -y ttf-gujarati-fonts')
os.system('apt-get remove -y ttf-punjabi-fonts')
os.system('apt-get remove -y ttf-sazanami-gothic')
os.system('apt-get remove -y ttf-sazanami-mincho')
os.system('apt-get remove -y ttf-tamil-fonts')
os.system('apt-get remove -y ttf-telugu-fonts')

# Remove httpd
os.system('apt-get remove -y apache2.2-bin libapache2-mod-dnssd')

# Remove java packages
os.system('apt-get remove -y liblucene2-java')

# Remove lisp
os.system('apt-get remove -y guile-1.8-libs')

# Remove mail apps
os.system('apt-get remove -y exim4-config')
os.system('apt-get remove -y procmail')
os.system('apt-get remove -y thunderbird thunderbird-l10n-en-us')

# Remove math apps
os.system('apt-get remove -y dc')
      
# Remove misc apps
os.system('apt-get remove -y grub2-theme-mint')
      
# Remove net apps
os.system('apt-get remove -y libpurple0 libpurple-bin pidgin-facebookchat pidgin-data')
os.system('apt-get remove -y samba samba-common samba-common-bin')
os.system('apt-get remove -y telepathy-gabble telepathy-mission-control-5 telepathy-salut')
os.system('apt-get remove -y xchat xchat-common')

# Remove ruby apps
os.system('apt-get remove -y libdpkg-ruby1.8 libgettext-ruby1.8 liblocale-ruby1.8')
os.system('apt-get remove -y libhttpclient-ruby1.8 libxml-parser-ruby1.8')
os.system('apt-get remove -y ruby ruby-xmlparser ruby1.8')

# Remove sound apps
os.system('apt-get remove -y espeak espeak-data libespeak1')

# Remove utility
os.system('apt-get remove -y inxi')

# Remove web apps
os.system('apt-get remove -y w3m')








      

      
      


      
      


print 'FINISHED REMOVING PACKAGES'
print '======================='
