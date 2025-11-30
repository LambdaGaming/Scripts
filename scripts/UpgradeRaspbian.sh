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
read -p "Enter the codename of your current Debian version: " current
read -p "Enter the codename of the Debian release you want to switch to: " release
sudo sed -i "s/$current/$release/g" /etc/apt/sources.list
sudo sed -i "s/$current/$release/g" /etc/apt/sources.list.d/raspi.list

# Start the upgrade
sudo apt update
sudo apt upgrade --without-new-pkgs
sudo apt full-upgrade
echo "Finished upgrade! Reboot as soon as possible."
