#!/usr/bin/node

import { argv } from 'node:process';

argv.forEach((val1, val2) => {
  console.log(`${val1} is ${val2}`);
});
