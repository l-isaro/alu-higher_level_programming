#!/bin/bash
# displays the size of the body 
curl -Is $1 | grep -i "content-length:" | cut -d " " f 2
