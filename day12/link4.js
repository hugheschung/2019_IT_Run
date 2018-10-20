//day12 練習4: findDocuments specific 
//1.link mongodb
//4.findDocuments const specific {'day9': 1}

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://localhost:27017';
// Database Name---
const dbName = 'HeartRate';
//	Collection Name---
const My_collection = 'h1f001';

const specific = {'day9': 1};  //查詢條件
//4.findDocuments add specific 
const findDocuments = function(db, callback) {
  // Get the documents collection  你要插入的collection名稱。
  const collection = db.collection(My_collection);
  // Find some specific documents 
  collection.find(specific).toArray(function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records");
    console.log(docs);
    callback(docs);
  });
}

//main---
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected correctly to server");

  const db = client.db(dbName);

//operations--
    findDocuments(db, function() {
      client.close();
    });
});
