#!/usr/bin/node

const args = process.argv.slice(2);
//prettier-ignore
function add (a, b) { 
  const result = parseInt(a) + parseInt(b);
  console.log(result);
}

add(args[0], args[1]);
