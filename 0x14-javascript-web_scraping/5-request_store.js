#!/usr/bin/node
// contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

request.get(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
