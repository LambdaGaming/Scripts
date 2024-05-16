#!/bin/bash
DEB=false

TarUpdate()
{
	URL="https://discord.com/api/download/stable?platform=linux&format=tar.gz"
	DIR="$(pwd)"

	while ! test -d "$DIR/Discord"; do
		read -p "Discord installation not found. Enter the path you want to install to, excluding the Discord folder: " DIR
	done

	echo "Downloading Discord..."
	wget -q --show-progress $URL -O /tmp/discord.tar.gz

	if test -f /tmp/discord.tar.gz; then
		echo "Extracting update..."
		tar -xf /tmp/discord.tar.gz
		echo "Cleaning up..."
		rm /tmp/discord.tar.gz
		rm -rf /tmp/Discord
		echo "Finished"
	else
		echo "Failed to download update. Aborting."
	fi
}

DebUpdate()
{
	URL="https://discord.com/api/download/stable?platform=linux&format=deb"
	echo "Downloading Discord..."
	wget -q --show-progress $URL -O /tmp/discord.deb
	
	if test -f /tmp/discord.deb; then
		echo "Installing update..."
		sudo dpkg -i /tmp/discord.deb
		echo "Cleaning up..."
		rm /tmp/discord.deb
		echo "Finished"
	else
		echo "Failed to download update. Aborting."
	fi
}

if command -v dpkg &> /dev/null; then
	DEB=true
fi

if "$DEB"; then
	DebUpdate
else
	TarUpdate
fi

read -p "Press any key to continue..."
