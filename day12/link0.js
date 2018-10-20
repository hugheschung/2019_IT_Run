//1.link mongodb

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');

// Connection URL
const url = 'mongodb://hughes:hughes123456@ds261332.mlab.com:61332/hughes_mongo';

// Database Name
const dbName = 'hughes_mongo';

//main--
// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  client.close();
});
