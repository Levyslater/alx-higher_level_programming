#!/bin/bash
# a bash script that sends a DELETE request to the url
# passed as the first argument and displays the body of the response
curl -sL -x "$1"