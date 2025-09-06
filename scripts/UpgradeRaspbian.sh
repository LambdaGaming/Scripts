#!/bin/bash

# Update and clean up current install
sudo apt update
sudo apt upgrade -y
sudo apt dist-upgrade -y
sudo apt clean
sudo apt autoremove -y

# Fix any potentially broken packages before upgrading
sudo apt --fix-broken install
sudo dpkg --configure -a

# Edit repo sources
read -p "Enter the codename of the Debian release you want to switch to: " release
src1="deb http://raspbian.raspberrypi.org/raspbian/ $release main contrib non-free rpi"
sudo sed -i "1s/.*/$src1/" /etc/apt/sources.list
src2="deb http://archive.raspberrypi.com/debian/ $release main"
sudo sed -i "1s/.*/$src2/" /etc/apt/sources.list.d/raspi.list

# Start the upgrade
sudo apt update
sudo apt upgrade --without-new-pkgs
sudo apt full-upgrade
echo "Finished upgrade! Reboot as soon as possible."
