#!/bin/bash
#SAMBA server admin script, NGC, last edit:20.02.2012

# }}}

# Define Colors {{{
RED='\e[1;31m'
blue='\e[0;34m'
BLUE='\e[1;34m'
cyan='\e[0;36m'
CYAN='\e[1;36m'
NC='\e[0m' # No Color
black='\e[0;30m'
BLACK='\e[1;30m'
green='\e[0;32m'
GREEN='\e[1;32m'
yellow='\e[0;33m'
YELLOW='\e[1;33m'
magenta='\e[0;35m'
MAGENTA='\e[1;35m'
white='\e[0;37m'
WHITE='\e[1;37m'
# }}}

menu () {
    MY_IP_LAN=$(/sbin/ifconfig eth0 | awk '/inet/ { print $2 } ' | sed -e s/addr://)
echo -e "${WHITE}//////////////////////////////////////////////////////"
echo            '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
echo
echo -e "   ${WHITE}Server : ${RED}$MY_IP_LAN" ${WHITE}
echo
echo ------------------------------------------------------
echo
echo -e
     uname -nsr
echo
echo
echo '//////////////////////////////////////////////////////'
echo '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
echo
echo ______________________________________________________
echo
echo -e "   ${YELLOW}[1]   ${WHITE}- ${RED} Rme -nsrESTART ${WHITE}SAMBA Server"
echo -e "   ${YELLOW}[2]   ${WHITE}- ${RED} STOP ${WHITE}SAMBA Server"
echo -e "   ${YELLOW}[3]   ${WHITE}- ${RED} START ${WHITE}SAMBA Server"
echo -e "   ${YELLOW}[4]   ${WHITE}- ${RED} Reload ${WHITE}smbd config files"
echo -e "   ${YELLOW}[5]   ${WHITE}- ${RED} View ${WHITE}Logged Users"
echo -e "   ${YELLOW}[6]   ${WHITE}- ${RED} Edit ${WHITE}smb.conf"
echo -e "   ${YELLOW}[7]   ${WHITE}- ${RED} View ${WHITE}passwd"
echo -e "   ${YELLOW}[a]   ${WHITE}- ${RED} ADD ${WHITE}user to the SAMBA Server"
echo -e "   ${YELLOW}[c]   ${WHITE}- ${RED} CHANGE ${WHITE}User Password for the SAMBA Server"
echo -e "   ${YELLOW}[e]   ${WHITE}- ${RED} ENABLE ${WHITE}user on the SAMBA Server"
echo -e "   ${YELLOW}[d]   ${WHITE}- ${RED} DISABLE ${WHITE}user on the SAMBA Server"
echo _______________________________________________________
echo
echo -e "   ${YELLOW}[n]    ${WHITE}- ${RED} Restart ${WHITE}NFS server"
echo -e "   ${YELLOW}[m]    ${WHITE}- ${RED} Reload ${WHITE}NFS config"
echo _______________________________________________________
echo
echo -e "   ${MAGENTA}[q]	- ${MAGENTA}EXIT script"${WHITE}
echo _______________________________________________________
#echo "	[w]	- Wipe user from the SAMBA Server"
}

 while true
  do
   menu
  read -p 'Operation : ' shibano

case "$shibano" in

################### Restart ####################
'1')
	 read -p 'See current state details? (y/n): ' -n 1 yn
	 echo
	if [ "$yn" == "y" ]
	 then
		/usr/bin/smbstatus -d >& /root/smbstatus.dump
		cat /root/smbstatus.dump
	fi
	  read -p 'Continue with RESTART ? (y/n): ' -n 1 yn
	  echo
	 if [ "$yn" == "y" ]
	  then
	       echo
	       echo SMBD restarting... && service smbd restart
	        sleep 1
	       echo
	       echo NMBD restarting... && service nmbd restart
                sleep 1
               echo
	       echo ----------DONE!------------
	       echo
	fi
	;;
#################### Stop #######################
'2')
         read -p 'See current state details? (y/n): ' -n 1 yn
         echo
        if [ "$yn" == "y" ]
         then
                /usr/bin/smbstatus -d >& /root/smbstatus.dump
                cat /root/smbstatus.dump
        fi
         read -p 'Are you shure you want to STOP ? (y/n): ' -n 1 yn
	 echo
	if [ "$yn" == "y" ]
         then
	        echo
	        echo SMBD stopping... && service smbd stop
	         sleep 1
		echo NMBD stopping... && service nmbd stop
		 sleep 1
		echo
		echo------------DONE!-------------
		echo
	fi
	;;
#################### Start #######################
'3')
         read -p 'Start SAMBA Server? (y/n): ' -n 1 yn
         echo
        if [ "$yn" == "y" ]
         then
                echo
                echo SMBD starting... && service smbd start
                 sleep 1
                echo NMBD starting... && service nmbd start
                 sleep 1
                echo
                echo------------DONE!-------------
                echo
        fi
        ;;

################### Reload conf ##################
'4')
	/usr/bin/smbstatus -b
	read -p 'Reload configuration? (y/n): ' -n 1 yn
	 echo
	if [ "$yn" == "y" ]
	 then
		service smbd reload
		echo
		echo ------------DONE!-------------
		echo
	fi
	;;
################# Status Check ################
'5')
	until [ "$another" == "n" ]
	do
		clear
		 /usr/bin/smbstatus -b | less
		  read -p 'More details (y/n): ' -n 1 yn
		   echo
		if [ "$yn" == "y" ]
		 then
			/usr/bin/smbstatus -d >& /root/smbstatus.dump
			less /root/smbstatus.dump
		fi
		 echo
		  read -p 'Check again ? (y/n): ' -n 1 another
		   echo
	done
	;;
################# Edit smb.conf #################
'6')
	if [ -f /etc/samba/smb.conf ]
	 then
		vim /etc/samba/smb.conf
	fi
 	;;
################# View users ####################
'7')
	if [ -f /etc/passwd ]
	 then
		less /etc/passwd
	fi
	;;
'a')
	until [ "$another" == "n" ]
	 do
		read -p 'User Name (8 characters max, small case, NO spacess): ' UserName
		 echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
		 echo 'User Name: '"$UserName"
		 echo
		read -p 'Is this OK ? (y/n): ' -n 1 yn
		 echo
		if [ "$yn" = "y" ]
		 then
			echo
			echo 'Adding User ....'
			useradd -m -b /home -s /sbin/nologin $UserName
			finger $UserName
			/usr/bin/smbpasswd -a -n $UserName
			echo
			/usr/bin/smbpasswd $UserName
		fi
		echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
		read -p 'Add another User ? (y/n): ' -n 1 another
		echo
		echo
	done
	;;
'c')
	echo 'CHANGE User Password'
	 read -p 'Enter User Name: ' UserName
	  /usr/bin/smbpasswd $UserName
	;;
'e')
	echo 'ENABLE User'
	 read -p 'Enter User Name: ' UserName
	  /usr/bin/smbpasswd -e $UserName
	;;
'd')
	echo 'DISABLE User'
	 read -p 'Enter User Name: ' UserName
	  /usr/bin/smbpasswd -d $UserName
	;;
'n')
	echo 'Restart the NFS server'
	 service nfs-kernel-server status >& /root/nfsstat.dump
                cat /root/nfsstat.dump
	sleep 3
		service nfs-kernel-server restart
	echo
	;;
'm')
	echo 'Reload NFS configuration'
	 	service nfs-kernel-server reload
	sleep 3
	echo
	;;
'w')################################################ Under Construction ###########################################
	if [ -f /usr/pkg/etc/samba/private/smbpasswd ]
	then
		echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
		read -p 'View smbpasswd file (y/n): ' -n 1 yn
		echo
		if [ "$yn" == "y" ]
		then
			less /usr/local/etc/samba/private/smbpasswd
			echo
		fi
	fi
	if [ -f /etc/master.passwd ]
	then
		echo
		echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
		read -p 'View master.passwd file (y/n): ' -n 1 yn
		echo
		if [ "$yn" == "y" ]
		then
			less /etc/master.passwd
			echo
		fi
	fi
	echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
	echo
	echo '!!! DELETE User !!!'
	read -p 'Enter User Name : ' UserName
	if [ -d /usr/samba/homes/$UserName ]
	then
		echo  ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
		echo 'File List of User Home:'
		ls -altT /usr/samba/homes/$UserName
		echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
		echo
		read -p 'Remove home directory (y/n): ' -n 1 yn
		echo
		if [ "$yn" == "y" ]
		then
			echo "Deleting:"
			rm -vr /usr/samba/homes/$UserName
			echo
		fi
		echo  ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

	fi
	echo
	/usr/local/bin/smbpasswd -x $UserName
	echo
	echo  ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
	read -p 'View smbpasswd file (y/n): ' -n 1 yn
	echo
	if [ "$yn" == "y" ]
	then
		less /usr/pkg/etc/samba/private/smbpasswd
		echo
	fi
	userdel $UserName
	echo  ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
	read -p 'View master.passwd file (y/n): ' -n 1 yn
	echo
	if [ "$yn" == "y" ]
	then
		less /etc/master.passwd
		echo
	fi
	;;
'q')

	exit
	;;

'f')
	echo
	echo "This is the end of your adventure!
The Samba server commits suicide with a spectacular fart, and you, my young friend, are wondering whether to ritually kill your self, die by sand [umri ot pesak], drink to get drunk till drop dead [umri ot pienye] or just to ignite and burn out the djapankite in a gallop to Sozopol ...
The choice is yours - enjoy it, regardless of that it is eternally fucked! :))) "
	echo
	exit
	;;
'g')
	echo "Under Construction !!!"
	;;
'h')
	echo "Under Construction !!!"
	;;
'i')
	echo "Under Construction !!!"
	;;
'j')
	echo "Under Construction !!!"
	;;
esac
done

