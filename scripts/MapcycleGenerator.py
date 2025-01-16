import os
import random
import re

def IsCampaignMap( map ):
	m = re.match( r'hldemo|[c|t][0-9]a[0-9]', map )
	if map.startswith( "hldemo" ) or m is not None:
		return True
	return False

mapList = []
for root, dirs, files in os.walk( os.getcwd() ):
	for file in files:
		if file.endswith( ".bsp" ) and not IsCampaignMap( file ):
			mapList.append( file.replace( ".bsp", "" ) )
random.shuffle( mapList )
with open( "mapcycle.txt", "w" ) as ms:
	ms.write( "\n".join( i for i in mapList ) )
print( "Successfully generated mapcycle.txt file to the current directory." )
