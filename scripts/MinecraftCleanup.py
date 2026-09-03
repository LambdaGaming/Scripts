import json
import os
import platform
import shutil
from pathlib import Path

def IsLinux():
	return platform.system() == "Linux"

def SafeRemoveFile( file ):
	if not os.path.exists( file ):
		return
	try:
		os.remove( file )
		print( f"Deleting {file}" )
	except PermissionError:
		print( f"Couldn't delete {file}: Permission denied." )
	except:
		print( f"Something went wrong while deleting {file}. Skipping..." )

AppData = IsLinux() and str( Path.home() ) or os.getenv( "APPDATA" )
MinecraftPath = AppData + "/.minecraft"
TechnicPath = AppData + "/.technic"
PrismPath = AppData + "/.local/share/PrismLauncher" if IsLinux() else "/PrismLauncher"

def DeleteOldVersions():
	# Get the latest release and snapshot versions so they aren't deleted
	print( "Checking for old Minecraft versions..." )
	path = MinecraftPath + "/versions/version_manifest_v2.json"
	if not os.path.exists( path ):
		print( f"Failed to detect Minecraft launcher. Probably not installed?" )
		return
	data = open( path, "r" )
	newJson = json.loads( data.read() )
	MostRecentVersion = newJson["latest"]["release"]
	MostRecentSnapshot = newJson["latest"]["snapshot"]
	data.close()

	# Parse launcher profiles
	path = MinecraftPath + "/launcher_profiles.json"
	data = open( path )
	newJson = json.loads( data.read() )
	profiles = newJson["profiles"]
	ProfileTable = []
	for profile in profiles:
		ProfileTable.append( newJson["profiles"][profile]["lastVersionId"] )

	# Delete unused versions
	versionPath = MinecraftPath + "/versions"
	getVersions = os.listdir( versionPath )
	for version in getVersions:
		finalPath = f"{versionPath}/{version}"
		if version in ProfileTable or version == MostRecentVersion or version == MostRecentSnapshot or not os.path.isdir( finalPath ):
			continue
		print( f"Deleting old Minecraft version: {version}" )
		shutil.rmtree( finalPath )

def DeleteLogs():
	# Minecraft launcher
	print( "Checking for Minecraft launcher logs..." )
	launcherLogPath = MinecraftPath + "/launcher_log.txt"
	SafeRemoveFile( launcherLogPath )
	logPath = MinecraftPath + "/logs"
	if os.path.exists( logPath ):
		getFiles = os.listdir( logPath )
		for file in getFiles:
			SafeRemoveFile( os.path.join( logPath, file ) )

	# Technic
	print( "Checking for Technic logs..." )
	logPath = TechnicPath + "/logs"
	if os.path.exists( logPath ):
		getFiles = os.listdir( logPath )
		for file in getFiles:
			SafeRemoveFile( os.path.join( logPath, file ) )
	modpackPath = TechnicPath + "/modpacks"
	print( "Checking for Technic modpack logs..." )
	if os.path.exists( modpackPath ):
		for modpack in os.listdir( modpackPath ):
			modpackLogPath = f"{modpackPath}/{modpack}/logs"
			logs = os.listdir( modpackLogPath )
			for l in logs:
				SafeRemoveFile( os.path.join( modpackLogPath, l ) )

	# Prism Launcher
	print( "Checking for Prism Launcher logs..." )
	logPath = PrismPath + "/logs"
	if os.path.exists( logPath ):
		getFiles = os.listdir( logPath )
		for file in getFiles:
			SafeRemoveFile( os.path.join( logPath, file ) )
	instancePath = PrismPath + "/instances"
	print( "Checking for Prism Launcher instance logs..." )
	if os.path.exists( instancePath ):
		for instance in os.listdir( instancePath ):
			if instance == ".tmp" or not os.path.isdir( f"{instancePath}/{instance}" ):
				continue
			instanceLogPath = f"{instancePath}/{instance}/minecraft/logs"
			if os.path.exists( instanceLogPath ):
				logs = os.listdir( instanceLogPath )
				for l in logs:
					SafeRemoveFile( os.path.join( instanceLogPath, l ) )

if __name__ == "__main__":
	print( "Minecraft Cleanup Utility | Copyright (c) 2020-2026 OPGman | Licensed under the MIT License" )
	DeleteOldVersions()
	DeleteLogs()
	print( "Process complete. Press any key to continue..." )
	input()
