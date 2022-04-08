#!/usr/bin/node
const request = requre("request");
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jsonResponse = JSON.parse(body).results;
    let count = 0;
    for (const movies in jsonResponse) {
      const chars = jsonResponse[movies].characters;
      for (const wedges in chars) {
        if (chars[wedges].includes("/18/")) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
