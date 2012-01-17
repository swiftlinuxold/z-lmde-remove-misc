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


def purge_packages(file):
    for line in open(file):
        os.system('apt-get purge -y ' + line)

purge_packages("lmde_not_lxde.txt")
# purge_packages("lmde_not_fluxbox.txt")

print 'FINISHED REMOVING MISC PACKAGES'
print '==============================='







      

      
      


      
      


print 'FINISHED REMOVING PACKAGES'
print '======================='
