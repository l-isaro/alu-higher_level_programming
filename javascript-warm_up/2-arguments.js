#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length > 1){
    console.log('Arguments found');
} else if (args.length == 0) {
    console.log("No argument");
} else {
    console.log("Argument found");
}
