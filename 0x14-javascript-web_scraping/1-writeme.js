#!/usr/bin/node

// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length < 4) {
  console.error('Usage: node script.js <file_path> <string_to_write>');
  process.exit(1);
}

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file asynchronously with UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Log the detailed error object if there is an error
    console.error(`[Error: ${err.message}] {`);
    console.error(`  errno: ${err.errno},`);
    console.error(`  code: '${err.code}',`);
    console.error(`  syscall: '${err.syscall}',`);
    console.error(`  path: '${err.path}'`);
    console.error('}');
    process.exit(1);
}
});
