#!/bin/bash

# Add routes for the connected networks
sudo route add -net 192.168.4.0/24 gw 192.168.4.254
sudo route add -net 192.168.6.0/24 gw 192.168.6.1
sudo route add -net 192.168.7.0/24 gw 192.168.7.1

# Display the updated routing table for verification
route -n

echo "Routing configuration has been updated on the router."
