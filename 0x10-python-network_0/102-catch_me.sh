#!/bin/bash
#cript that makes a request that causes the server to respond You got me!
curl -sL -X PUT -d user_id=98 -H "Origin: HolbertonSchool" "$1"
