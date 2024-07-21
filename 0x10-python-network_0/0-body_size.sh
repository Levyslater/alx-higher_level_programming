#!/bin/bash
# a bash script that takes in a url, sends a request to the url
# and displays the size of body of the response
curl -sL "$1" | wc -c