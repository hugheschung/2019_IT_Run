//1.link mongodb
//2.insertDocuments
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://localhost:27017';
// Database Name---
const dbName = 'HeartRate';

//2.insertDocuments
const insertDocuments = function(db, callback) {
  // Get the documents collection
  const collection = db.collection('h1f001');
  // Insert some documents
  collection.insertMany([
    {day9 : 1}, {day10 : 2}, {day11 : 3}
  ], function(err, result) {
    assert.equal(err, null);
    assert.equal(3, result.result.n);
    assert.equal(3, result.ops.length);
    console.log("Inserted "+ result.result.n +" documents into the collection");
    callback(result);
  });
}


//main---
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");

  const db = client.db(dbName);
  //operations--
  //Insert some documents
  insertDocuments(db, function() {
    client.close();
  });

});
