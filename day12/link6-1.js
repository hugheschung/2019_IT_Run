//day12 練習6-1: removeDocument  移除多筆資料練習
//1.link mongodb
//6.removeDocument

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://localhost:27017';
// Database Name---
const dbName = 'HeartRate';
//	Collection Name---
const My_collection = 'h1f001';


//6.removeDocument
const removeDocument = function(db, callback) {
  // Get the documents collection
  const collection = db.collection(My_collection);
  // Delete document 
  collection.deleteMany({ day9 : 1 }, function(err, result) {
    assert.equal(err, null);
    //assert.equal(1, result.result.n);
    console.log("Removed the document");
    callback(result);
  });
}


//main---
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected correctly to server");

  const db = client.db(dbName);

//operations--
removeDocument(db, function() {
    client.close();
  });
});
