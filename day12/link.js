//1.link mongodb
//7.index to Collection

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://hughes:hughes123456@ds261332.mlab.com:61332/hughes_mongo';
// Database Name---
const dbName = 'hughes_mongo';
//add const document = 'demo' replace func();
const documents = 'demo';

//7.indexCollection
const indexCollection = function(db, callback) {
  db.collection(documents).createIndex(
    { "i": 1 },
      null,
      function(err, results) {
        console.log(results);
        callback();
    }
  );
};

//main---
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected correctly to server");

  const db = client.db(dbName);

//operations--
indexCollection(db, function() {
      client.close();
    });
});
