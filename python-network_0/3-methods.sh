#!/bin/bash
# returns all methods that the server will accept
curl -sI $1 | grep -i "allow:" | curt -d ":" -f 2
