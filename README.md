# Linux
## [Save List of Installed Packages](scripts/GetInstalledPackages.sh)
 Saves text files containing a list of packages installed on your system to your downloads folder. Supports all major package managers including apt, dnf, flatpak, pacman, and snap.

## [Restart KDE Plasma](scripts/RestartPlasma.sh)
 Restarts the KDE Plasma shell. Works with version 5.10 and newer.

## [System Cleanup](scripts/SystemCleanup.sh)
 Cleans caches, logs, temporary files, and other unnecessary system files.

## [Discord Auto-Updater](scripts/UpdateDiscord.sh)
 Automatically updates Discord and supports both tar.gz and deb installations. For a tar.gz installation, if Discord is found in the current working directory, the script will install the update to that location, otherwise it will prompt the user to enter a path. The script will terminate if the download fails for whatever reason.

## [Update Arch Mirrors](scripts/UpdateMirrors.sh)
 Updates and ranks the Pacman mirror list using Reflector, then refreshes all packages. Has optional support for EndeavourOS using the eos-rankmirrors tool.

# Windows
## [OSDATA Bluescreen Demo](scripts/OSDATADemo.bat)
 Demonstrates how the an improperly formatted OSDATA system config file can cause a bluescreen on startup. It creates the file, writes garbage data to it, then reboots Windows. The effect can be reverted by deleting the created OSDATA file through the recovery settings. This only works on Windows 10 and 11, and needs to be run as admin if you're not already on an admin account.

## [Update Python Packages](scripts/UpdatePythonPackages.ps1)
 Updates every Python package that was installed through pip.

# Raspberry Pi
## [I2C and SPI Dump Examples](scripts/DumpExamples.sh)
 Various example commands for dumping data from I2C and SPI chips.

## [Upgrade Raspberry Pi OS](scripts/UpgradeRaspbian.sh)
 Upgrades Raspberry Pi OS to a specified Debian release. Should work with Debian 9 and newer. Upgrading this way isn't recommened as things could break to the point where reinstalling the whole OS would be easier than trying to fix it, but if you don't have any weird configs or manually installed packages then you'll *probably* be fine. This could probably also be used for vanilla Debian with a few minor tweaks.

# System-Agnostic
## [Extract Files From Jellyfin Playlist](scripts/JellyfinPlaylistExtractor.py)
 Extracts files from a specified Jellyfin playlist file. For maximum compatibility with other systems (car radios for example), all files are placed in a single folder and certain characters are stripped from file names. Multiple files with the same name will be renamed to avoid conflicts. Requires Python 3.6+ with the humanfriendly module.

## [mapcycle.txt Generator](scripts/MapcycleGenerator.py)
 Generates mapcycle.txt files for GoldSrc and Source engine multiplayer games. It reads all .bsp files in the current directory and adds them to the mapcycle.txt file in a random order. Half-Life 1 singleplayer maps are ignored. Requires Python 2.5+ or any Python 3 version.

## [Minecraft Cleanup Utility](scripts/MinecraftCleanup.py)
 Scans for log files from Minecraft Java Edition and Technic Launcher, and removes any that are found. Will also delete unused versions of Minecraft Java Edition that aren't found in the version_manifest_v2.json file. You can launch the script with the -y parameter to bypass the prompts. Requires Python 3.6+.

## [Cleanup Unused Gmod Server Addons](scripts/ServerGMACleanup.py)
 Removes unused downloaded GMA files from Garry's Mod dedicated servers, similarly to the menu_cleanup command on the client. References to removed addons are also removed from the appworkshop_4000.acf file to avoid issues downloading them again in the future. The script will prompt for a workshop collection ID and path to the server, but they can also be passed as parameters. The specified workshop collection __must__ be public; unlisted collections will not work. Requires Python 3.6+ and the humanfriendly, requests, and vdf modules.

## [Regenerate Expired Steam Server Tokens](scripts/SteamTokenGenerator.py)
 Generates a new Steam server token for each expired token that is found. A Steam app ID and your Steam web API key need to be passed as parameters. Each generated token will be saved to a text file in your documents folder. Requires Python 3.6+ and the requests module.
