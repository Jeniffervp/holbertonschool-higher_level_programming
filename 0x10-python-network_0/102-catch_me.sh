#!/bin/bash
#cript that makes a request that causes the server to respond You got me!
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
