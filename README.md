# Linux
## [Save List of Installed Packages](scripts/GetInstalledPackages.sh)
 Saves text files containing a list of packages installed on your system to your downloads folder. Supports all major package managers including apt, dnf, flatpak, pacman, and snap.

## [System Cleanup](scripts/SystemCleanup.sh)
 Cleans caches, logs, temporary files, and other unnecessary system files.

## [Discord Auto-Updater](scripts/UpdateDiscord.sh)
 Automatically updates Discord and supports both tar.gz and deb installations. For a tar.gz installation, if Discord is found in the current working directory, the script will install the update to that location, otherwise it will prompt the user to enter a path. The script will terminate if the download fails for whatever reason.

## [Update Arch Mirrors](scripts/UpdateMirrors.sh)
 Updates and ranks the Pacman mirror list using Reflector, then refreshes all packages. Has optional support for EndeavourOS using the eos-rankmirrors tool.

## [yt-dlp Wrapper](scripts/YtdlpWrapper.sh)
 Simple wrapper script for yt-dlp that automatically handles multiple URLs and output file formatting. All files are output to ~/Downloads.

# Raspberry Pi
## [I2C and SPI Dump Examples](scripts/DumpExamples.sh)
 Various example commands for dumping data from I2C and SPI chips.

# OS-Agnostic
## [Extract Files From Jellyfin Playlist](scripts/JellyfinPlaylistExtractor.py)
 Extracts files from a specified Jellyfin playlist file. For maximum compatibility with other systems (car radios for example), all files are placed in a single folder and certain characters are stripped from file names. Multiple files with the same name will be renamed to avoid conflicts. Requires Python 3.6+ with the humanfriendly module.

## [mapcycle.txt Generator](scripts/MapcycleGenerator.py)
 Generates mapcycle.txt files for GoldSrc and Source engine multiplayer games. It reads all .bsp files in the current directory and adds them to the mapcycle.txt file in a random order. Half-Life 1 singleplayer maps are ignored. Requires Python 2.5+ or any Python 3 version.

## [Minecraft Cleanup Utility](scripts/MinecraftCleanup.py)
 Cleans up log files from the Minecraft Launcher, Technic Launcher, and Prism Launcher. Will also delete unused versions of Minecraft Java Edition that aren't found in the version_manifest_v2.json file. Requires Python 3.6+.

## [Cleanup Unused Gmod Server Addons](scripts/ServerGMACleanup.py)
 Removes unused downloaded GMA files from Garry's Mod dedicated servers, similarly to the menu_cleanup command on the client. References to removed addons are also removed from the appworkshop_4000.acf file to avoid issues downloading them again in the future. The script will prompt for a workshop collection ID and path to the server, but they can also be passed as parameters. The specified workshop collection __must__ be public; any other visibility setting will not work. Requires Python 3.6+ and the humanfriendly, requests, and vdf modules.

## [Regenerate Expired Steam Server Tokens](scripts/SteamTokenGenerator.py)
 Generates a new Steam server token for each expired token that is found. A Steam app ID and your Steam web API key need to be passed as parameters. Each generated token will be saved to a text file in your documents folder. Requires Python 3.6+ and the requests module.

## [Songsterr Auto Clicker](scripts/SongsterrClicker.js)
 TamperMonkey script that automatically clicks popups on Songsterr. It does NOT block the popup from appearing; it can still appear for up to 1 second each time. Only tested on Firefox but should work on any browser.

# Contributing
 Contributions are welcome! Please read through the [guidelines](https://lambdagaming.github.io/guides/contributing) before submitting an issue or pull request.
