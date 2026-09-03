#!/bin/bash
read -a list -p "Enter links (separate with space): "
read -p "Enter type (mp3, mp4, aac, mkv): " type
for l in ${list[*]}; do
    yt-dlp -P ~/Downloads -t "$type" -o "%(title)s.%(ext)s" --restrict-filenames "$l"
done
echo "Finished"
