#!/bin/bash
# returns all methods that the server will accept
curl -s $1 | grep -i "allow:" | cut -d ":" -f 2
