#!/bin/bash
ip="" # IP address of the target server
mac="" # MAC address of the target's network interface
port="" # Port to scan to detect when the server is up
echo "Starting server..."
wakeonlan -i $ip $mac
echo "Waiting for signal..."
until nc -vzw 2 $ip $port; do sleep 2; done
echo "Server up!"
