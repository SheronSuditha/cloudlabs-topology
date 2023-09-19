#!/bin/bash

# Add a default route via the router
sudo route add default gw 192.168.8.1

# Display the updated routing table for verification
route -n

echo "Routing configuration has been updated on the server."
