#!/bin/bash
# takes in a URL as an argument, sends a GET request to URL
curl -sX GET -H "X-School-User-Id: 98" "$1"
