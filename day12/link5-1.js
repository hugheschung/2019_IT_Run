//day12 練習5-1: updateDocument  更新多筆資料練習
//1.link mongodb
//5.updateDocument  

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://localhost:27017';
// Database Name---
const dbName = 'HeartRate';
//	Collection Name---
const My_collection = 'h1f001';

//5.updateDocument
const updateDocument = function(db, callback) {
  // Get the documents collection
  const collection = db.collection(My_collection);
  // Update many document where day9 is 1, set b equal to your setting
  collection.updateMany(
						{ day9 : 1 }, 
						{ $set: { b : "hello!!你好嗎?" } }, 
						function(err, result) 
							{
								assert.equal(err, null);
								//assert.equal(1, result.result.n);
								console.log("Updated the document");
								callback(result);
							});
}


//main---
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected correctly to server");

  const db = client.db(dbName);

//operations--
updateDocument(db, function() {
    client.close();
  });
});
