#!/bin/bash
#  script that sends a request to a URL, and displays the size of the body
curl -sD - "$1" | grep Content-Length: | cut -d " " -f2
