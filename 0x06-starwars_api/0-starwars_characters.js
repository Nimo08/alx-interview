#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  body.characters.forEach((charUrl) => {
    request(charUrl, { json: true }, (error, response, character) => {
      if (error) {
        console.error(error);
      } else {
        console.log(character.name);
      }
    });
  });
});
