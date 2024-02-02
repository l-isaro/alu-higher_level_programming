#!/usr/bin/node

const args = process.argv.slice(2);
function add(a, b) {
  let result = parseInt(a) + parseInt(b);
  console.log(result);
}

add(args[0], args[1]);
