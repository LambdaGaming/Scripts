#!/bin/bash
sudo rm -rf /var/lib/systemd/coredump
sudo rm -rf /var/log/*
sudo rm -rf /var/cache/*
sudo rm -rf /var/tmp/*
flatpak uninstall --unused -y
echo Finished
read -p "Press any key to continue..."
