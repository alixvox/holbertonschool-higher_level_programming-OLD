#!/usr/bin/node
const fileserver = require("fs");
file.server.readFile(process.argv[2], "utf-8", function (error, content) {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
