#!/usr/bin/node

const args = process.argv.slice(2);

if (parseInt(args[0])) {
  for (let index = 0; index < parseInt(args[0]); index++) {
    console.log('X'.repeat(parseInt(args[0])));
  }
} else {
  console.log('Missing size');
}
