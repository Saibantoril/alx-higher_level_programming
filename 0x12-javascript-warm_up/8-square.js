#!/usr/bin/node

const size = process.argv[2];

if (!size || isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  const parsedSize = parseInt(size);
  let row = '';

  for (let i = 0; i < parsedSize; i++) {
    row += 'X';
  }

  for (let i = 0; i < parsedSize; i++) {
    console.log(row);
  }
}
