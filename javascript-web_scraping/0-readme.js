#!/usr/bin/node

const args = process.argv.slice(2);
const { error } = require('node:console');
const fs = require('node:fs');

fs.readFile(args, 'utf-8', (err, data) => {
  if (error) {
    console.error(err);
  } else {
    console.log(data);
  }
})
