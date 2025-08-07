# Linux
## [Save List of Installed Packages](scripts/GetInstalledPackages.sh)
- Saves text files containing a list of packages installed on your system to your downloads folder
- Supports all major package managers including apt, dnf, flatpak, pacman, and snap

## [Restart KDE Plasma](scripts/RestartPlasma.sh)
- Restarts the KDE Plasma shell, works with version 5.10 and newer

## [System Cleanup](scripts/SystemCleanup.sh)
- Cleans caches, logs, temporary files, and other unnecessary system files

## [Discord Auto-Updater](scripts/UpdateDiscord.sh)
- Supports both tar.gz and deb installations
- For a tar.gz installation, if Discord is found in the current working directory, the script will install the update to that location, otherwise it will prompt the user to enter a path
- The script will terminate if the download fails for whatever reason
- Useful for when your package manager's version isn't up to date but the app forces you to update

# Windows
## [OSDATA Bluescreen Demo](scripts/OSDATADemo.bat)
- Demonstrates how the an improperly formatted OSDATA system config file can cause a bluescreen on startup
- Creates the file then instantly reboots Windows
- Can be reverted by deleting the created OSDATA file through the recovery settings
- Works on Windows 10 and 11
- Needs to be run as admin if not already on an admin account

## [Update Python Packages](scripts/UpdatePythonPackages.ps1)
- Updates every Python package that was installed through pip

# Raspberry Pi
## [I2C and SPI Dump Examples](scripts/DumpExamples.sh)
- Various example commands for dumping data from I2C and SPI chips

# System-Agnostic
## [Extract Files From Jellyfin Playlist](scripts/JellyfinPlaylistExtractor.py)
- Extracts files from a specified jellyfin playlist file
- For maximum compatibility, all files are placed in a single folder and certain characters are stripped from file names
- Multiple files with the same name will be renamed to avoid conflicts
- Requires Python 3.6+ and the humanfriendly module

## [mapcycle.txt Generator](scripts/MapcycleGenerator.py)
- Generates mapcycle.txt files for GoldSrc and Source engine multiplayer games
- Reads all .bsp files in the current directory and adds them to the mapcycle.txt file in a random order
- Half-Life 1 singleplayer maps are ignored
- Requires Python 2.5+ or any Python 3 version

## [Minecraft Cleanup Utility](scripts/MinecraftCleanup.py)
- Removes log files from Minecraft Java Edition and the Technic Launcher
- Scans the Minecraft Launcher for Java Edition versions and deletes any versions that aren't found in the list
- Launch the script with the -checkall parameter to bypass all prompts
- Requires Python 3.6+

## [Cleanup Unused Gmod Server Addons](scripts/ServerGMACleanup.py)
- Removes unused downloaded GMA files from Garry's Mod dedicated servers
- References to removed addons are also removed from the appworkshop_4000.acf file to avoid issues downloading them again in the future
- Will prompt for a workshop collection ID and path to server but they can also be passed as parameters
- The specified workshop collection MUST be set to public
- Requires Python 3.6+ and the humanfriendly, requests, and vdf modules

## [Regenerate Expired Steam Server Tokens](scripts/SteamTokenGenerator.py)
- Generates a new Steam server token for each expired token that is detected
- Need to pass a Steam app ID and your Steam web API key as parameters
- Each generated token will be saved to a text file in your documents folder
- Requires Python 3.6+ and the requests module
