#!/usr/bin/node

const arguments = process.argv.slice(2);

if (arguments) {
    console.log(arguments);
} else {
    console.log('No argument');
}