#!/bin/bash

# Enable IP forwarding
sysctl net.ipv4.ip_forward=1

# Add a route to the client network
ip route add 192.168.4.0/24 via 192.168.4.1

# Add a route to the server network
ip route add 192.168.8.0/24 via 192.168.8.2