const fetch = require('node-fetch');

const headers = {
  'Accept':'application/json'

};

fetch('https://sat-api.developmentseed.org/stac',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});