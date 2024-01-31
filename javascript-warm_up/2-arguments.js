#!/usr/bin/node
const arguments = process.argv.slice(2);
const num_args = arguments.length

if (num_args > 1){
    console.log('Arguments found');
} else if (num_args == 0) {
    console.log("No argument");
} else {
    console.log("Argument found");
}
