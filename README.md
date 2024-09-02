# Miscellaneous Scripts
 Various scripts used for a variety of purposes. Below is a list of everything.

## I2C and SPI Dump Examples (DumpExamples.sh)
- Various example commands for dumping data from I2C and SPI chips using a Raspberry Pi

## Save List of Installed Packages (GetInstalledPackages.sh)
- Saves text files containing a list of packages installed on your system to your downloads folder
- Supports all major package managers including apt, dnf, flatpak, pacman, and snap

## Restart KDE Plasma (RestartPlasma.sh)
- Restarts the KDE Plasma shell, works with version 5.10 and newer

## Linux System Cleanup (SystemCleanup.sh)
- Cleans caches, logs, temporary files, and other unnecessary system files

## Discord Auto-Updater for Linux (UpdateDiscord.sh)
- Supports both tar.gz and deb installations
- For a tar.gz installation, if Discord is found in the current working directory, the script will install the update to that location, otherwise it will prompt the user to enter a path
- The script will terminate if the download fails for whatever reason
- Useful for when your package manager's version isn't up to date but the app forces you to update
