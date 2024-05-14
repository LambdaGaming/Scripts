#!/bin/bash
URL="https://discord.com/api/download/stable?platform=linux&format=tar.gz"
DIR=$(command -v Discord)

if [[ ${#DIR} -ge 16 ]]; then
	DIR=${DIR:0:-16}
fi

while ! test -d "$DIR"; do
	read -p "Discord installation not found. Enter the path you want to install to, excluding the Discord folder: " DIR
done

cd "$DIR"
echo "Downloading Discord..."
wget -q --show-progress $URL -O /tmp/discord.tar.gz

if test -f /tmp/discord.tar.gz; then
	echo "Extracting update..."
	tar -xf /tmp/discord.tar.gz
	echo "Adding program to PATH..."
	PATH="$DIR/Discord":$PATH
	echo "Cleaning up..."
	rm /tmp/discord.tar.gz
	rm -rf /tmp/Discord
	echo "Finished"
else
	echo "Failed to download update. Aborting."
fi

read -p "Press any key to continue..."
