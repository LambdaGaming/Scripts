#!/bin/bash
if command -v eos-rankmirrors &> /dev/null; then
	eos-rankmirrors
fi
sudo reflector --country US --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
sudo pacman -Syyu
