#!/bin/bash

# Accept connections from the router
iptables -A INPUT -s 192.168.8.0/24 -j ACCEPT

# Accept connections from the clients
iptables -A INPUT -s 192.168.4.0/24 -j ACCEPT

# Respond to ICMP ping requests
iptables -A OUTPUT -p icmp --icmp-type echo-request -j ACCEPT