#!/usr/bin/node

const args = process.argv.slice(2);
const { error } = require('node:console');
const fs = require('node:fs');

const file_content = fs.readFileSync(args[0], 'utf-8', (error, data) => {
  if(error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
