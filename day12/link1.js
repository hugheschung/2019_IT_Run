//1.link mongodb
//2.insertDocuments
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://hughes:hughes123456@ds261332.mlab.com:61332/hughes_mongo';
// Database Name---
const dbName = 'hughes_mongo';

//2.insertDocuments
const insertDocuments = function(db, callback) {
  // Get the documents collection
  const collection = db.collection('demo');
  // Insert some documents
  collection.insertMany([
    {t : 1}, {t : 2}, {t : 3}
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
