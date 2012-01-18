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

print '============================'
print 'BEGIN REMOVING MISC PACKAGES'

# Remove Thunderbird (email suite)
os.system('apt-get purge -y thunderbird thunderbird-l10n-en-us')

# Remove XChat
os.system('apt-get purge -y xchat-common xchat')
      
# Remove GIMP
os.system('apt-get purge -y gimp gimp-data libgimp2.0')
os.system('apt-get purge -y cups-driver-gutenprint libgutenprint2')
os.system('apt-get purge -y libgtk2-perl libgnome2-canvas-perl libgnome2-perl')

# Remove Samba
os.system('apt-get remove -y samba samba-common samba-common-bin')

# Remove Telepathy
os.system('apt-get remove -y libtelepathy-glib0 vino')
os.system('apt-get remove -y telepathy-mission-control-5 telepathy-gabble telepathy-salut')
      
      
     
      


# Remove C compilers (GCC, etc.)

# Remove selected packages from the editors section
os.system('apt-get remove -y nano vim-common vim-tiny')

# Remove selected packages from the font section
os.system('apt-get remove -y ttf-bengali-fonts')
os.system('apt-get remove -y ttf-gujarati-fonts')
os.system('apt-get remove -y ttf-punjabi-fonts')
os.system('apt-get remove -y ttf-sazanami-gothic')
os.system('apt-get remove -y ttf-sazanami-mincho')
os.system('apt-get remove -y ttf-tamil-fonts')
os.system('apt-get remove -y ttf-telugu-fonts')

# Remove packages from httpd section
os.system('apt-get remove -y apache2.2-bin libapache2-mod-dnssd')

# Remove selected packages (cpp) from the interpreter section
os.system('apt-get remove -y cpp-4.3 gcc-4.3')

# Remove packages from lisp section
os.system('apt-get remove -y guile-1.8-libs')

# Remove selected packages from the mail section
os.system('apt-get remove -y exim4-config procmail')

# Remove selected packages from the math section
os.system('apt-get remove -y dc')

# Remove packages from ruby section
os.system('apt-get remove -y libdpkg-ruby1.8 libgettext-ruby1.8 liblocale-ruby1.8')
os.system('apt-get remove -y libhttpclient-ruby1.8 libxml-parser-ruby1.8')
os.system('apt-get remove -y ruby ruby-xmlparser ruby1.8')      
      

#def purge1(package):
#    print 'FAKEpurging ' + package
#    os.system('apt-get purge -y ' + package)

#def purge_packages_2(file):
#    for line in open(file):
#        print 'PURGING ' + line
#        os.system('apt-get purge -s ' + line)

# purge_packages_2("lmde_not_lxde.txt")
# purge_packages("lmde_not_fluxbox.txt")

print 'FINISHED REMOVING MISC PACKAGES'
print '==============================='


