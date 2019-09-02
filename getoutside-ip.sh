#!/bin/bash
#
# Output public IP from behind NAT using checkip.dyndns.org
#
printf "Your Current IP address is: "
curl -s http://checkip.dyndns.org | awk '{print $4,$5,$6}' | cut -c 12-25
#
# Respect for opensource... Respect for sharing!!
# Script written by Sergani ... msergani@gmail.com, updated by Rick Osteen
