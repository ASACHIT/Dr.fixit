#!/bin/bash
echo "Checking for update in Github"
git pull origin master
pwd
chmod +x ./update.sh
cd ..
pwd
echo -e "Done"
sleep 2
python3 DRFIXIT.py