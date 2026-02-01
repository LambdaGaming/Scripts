import copy
import humanfriendly
import json
import os
import pathlib
import requests
import shutil
import sys
import vdf

if __name__ == "__main__":
	TotalSize = 0
	global CollectionID
	global ServerPath

	if len( sys.argv ) <= 1:
		CollectionID = input( "Collection ID parameter not specified. Please enter it now: " )
	else:
		CollectionID = sys.argv[1]

	if len( sys.argv ) >= 3:
		os.chdir( os.path.expanduser( sys.argv[2] ) )

	if not os.path.exists( "srcds.exe" ) and not os.path.exists( "srcds_run" ):
		print( "ERROR: Script is not in root folder of server." )
		input( "Press any key to continue..." )
		sys.exit()

	print( "Gathering collection info..." )
	url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"
	data = { "collectioncount": "1", "publishedfileids[0]": CollectionID }
	collectionList = requests.post( url, data )

	j = json.loads( collectionList.text )
	children = j["response"]["collectiondetails"][0]["children"] if "children" in j["response"]["collectiondetails"][0] else None

	if children is None:
		print( "ERROR: Empty collection detected. Make sure it's public and try again." )
		input( "Press any key to continue..." )
		sys.exit()

	print( "Gathering addon info..." )
	addonIDs = []
	for addon in children:
		addonIDs.append( addon["publishedfileid"] )

	addonTxt = vdf.load( open( "garrysmod/cfg/srcds_addons.txt" ) )["srcds_addons"]
	addonList = []
	gameCache = []
	workshopCache = []

	print( "Scanning game cache..." )
	for path, dirs, files in os.walk( "garrysmod/cache/srcds" ):
		for name in files:
			if os.path.splitext( name )[0] not in addonIDs:
				finalPath = os.path.join( path, name )
				TotalSize += os.path.getsize( finalPath )
				gameCache.append( finalPath )
				addonList.append( os.path.splitext( name )[0] )

	print( "Scanning Steam workshop cache..." )
	for path, dirs, files in os.walk( "steam_cache/content/4000" ):
		for name in dirs:
			if name not in addonIDs:
				finalPath = os.path.join( path, name )
				for file in pathlib.Path( finalPath ).rglob( '*' ):
					TotalSize += file.stat().st_size
				workshopCache.append( finalPath )
				addonList.append( name )

	if len( addonList ) == 0:
		print( "No unused files detected." )
		input( "Press any key to continue..." )
		sys.exit()

	print( "\nThe following addons are unused and are no longer required:" )
	for addon in addonList:
		name = addonTxt[addon]["name"] if addon in addonTxt and "name" in addonTxt[addon] else "Unknown Addon"
		print( f"{name} ({addon})" )
	
	if input( "\nContinue? (y/n)" ) == "n":
		sys.exit()

	for path in gameCache:
		os.remove( path )
		print( f"Removing {path}" )
	for path in workshopCache:
		shutil.rmtree( path )
		print( f"Removing {path}" )

	print( "\nUpdating workshop manifest file..." )
	acf = vdf.load( open( "steam_cache/appworkshop_4000.acf" ) )
	temp = copy.deepcopy( acf )
	for id in acf["AppWorkshop"]["WorkshopItemsInstalled"]:
		if id not in addonIDs:
			del temp["AppWorkshop"]["WorkshopItemsInstalled"][id]
	for id in acf["AppWorkshop"]["WorkshopItemDetails"]:
		if id not in addonIDs:
			del temp["AppWorkshop"]["WorkshopItemDetails"][id]
	vdf.dump( temp, open( "steam_cache/appworkshop_4000.acf", "w" ), True )

	print( "Finished!" )
	print( f"Total storage saved: {humanfriendly.format_size( TotalSize )}" )
	input( "Press any key to continue..." )
