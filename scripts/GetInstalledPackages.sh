#!/bin/bash

IsInstalled()
{
    if command -v $1 &> /dev/null; then
	    return 0
    fi
    return 1
}

cd ~/Downloads
if IsInstalled apt; then
    apt list --installed > installed_apt.txt
fi
if IsInstalled dnf; then
    dnf list installed > installed_dnf.txt
fi
if IsInstalled flatpak; then
    flatpak list > installed_flatpak.txt
fi
if IsInstalled pacman; then
    pacman -Q > installed_pacman.txt
fi
if IsInstalled snap; then
    snap list > installed_snap.txt
fi
