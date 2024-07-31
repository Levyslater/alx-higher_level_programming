#!/usr/bin/node

// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length < 3) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the file asynchronously with UTF-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Log the detailed error object
    console.error(`[Error: ${err.message}] {`);
    console.error(`  errno: ${err.errno},`);
    console.error(`  code: '${err.code}',`);
    console.error(`  syscall: '${err.syscall}',`);
    console.error(`  path: '${err.path}'`);
    console.error('}');
    process.exit(1);
  }
  // Log the file content to the console
  console.log(data);
});
