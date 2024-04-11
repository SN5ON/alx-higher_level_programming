#!/usr/bin/node
const count = [];
exports.logMe = function (item) {
  console.log(count.length + ': ' + item);
  count[count.length] = item;
};
