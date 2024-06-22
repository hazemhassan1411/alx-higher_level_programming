#!/usr/bin/node
/* hiii */
const args = process.argv.slice(2);
const firstarg = args[0];

if (isNaN(parseInt(firstarg))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(firstarg)}`);
}
