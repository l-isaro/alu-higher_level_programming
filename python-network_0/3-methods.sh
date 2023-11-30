#!/bin/bash
# returns all methods that the server will accept
curl -sI $1 | grep -i "allow:" | cut -d ":" -f 2
