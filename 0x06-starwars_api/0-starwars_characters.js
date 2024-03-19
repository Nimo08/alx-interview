#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const api_url = 'https://swapi-api.alx-tools.com/api/films/';

if (process.argv.length > 2) {
  request(`${api_url}${movieID}/`, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const charURL = JSON.parse(body).characters;
    const charName = charURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (error, response, charBody) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(charBody).name);
        });
      }));

    Promise.all(charName)
      .then(names => console.log(names.join('\n')))
      .catch(error => console.log(error));
  });
}
