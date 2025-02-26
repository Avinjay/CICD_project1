#!/usr/bin/bash
var=`echo "$1" | cut -f2 -d "/" | cut -f1 -d "." `
#log=`ls -rlth filelo* | tail -1 | awk -F " " '{ print $9}'`
logpath=`pwd`
GITPATH=/home/avinjay/GIT/
filename=`ls -rlth filelo* | tail -1 | awk -F " " '{ print $9}'`
log=$logpath/$filename
echo "$log"
echo "deployment begins now, deploy script from bash called" >> "$log"
pwd
ls -ld CICD_project1
if [ $? -eq 0 ]; then
	echo "local repo "$var"  exist ,thus pull request initiated" | tee -a "$log"
	cd "$var"
	pwd
	git pull origin main >> "$log"
	if [ $? -eq 0 ]; then
		echo "GIT Pull completed successfully" | tee -a "$log"
		sudo cp -p index.html /var/www/html/
        	sudo systemctl restart nginx
		if [ $? -eq 0 ]; then
			echo "Index.html placed and service restarted" | tee -a "$log"
		fi
	else
		echo "error pulling repo" >> "$log"
	fi
else
	cd "GITPATH"
	git clone $1
	if [ $? -eq 0 ]; then
	       echo "GIT repo clone on local completed" | tee -a "$log"	
		var=`echo "$1" | cut -f2 -d "/" | cut -f1 -d "." ` 
		cd "$var"
		sudo cp -p index.html /var/www/html/
		sudo systemctl restart nginx
		if [ $? -eq 0 ]; then
			echo "Index.html placed and service restarted" | tee -a "$log"
		fi
	fi
fi	
