#!/usr/bin/node

const OriginalSquare = require('./5-square');

module.exports = class Square extends OriginalSquare {
  constructor() {
    super(size);
  }
  charprint (c) {
    if (c) {
      for (let index = 0; index < this.height; index++) {
        console.log('C'.repeat(this.width));
        
      }
    } else {
      for (let index = 0; index < this.height; index++) {
        console.log('X'.repeat(this.width));
        
      }
    }
  }
};
