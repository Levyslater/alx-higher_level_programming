#!/usr/bin/bash

# A Bash script that takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
