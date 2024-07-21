#!/usr/bin/bash
# A bash script that takes in a URL and displays all
# HTTP methods the server will accept
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
