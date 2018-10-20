//day12 練習3: findDocuments
//1.link mongodb
//3.findDocuments  查找資料指令


const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://localhost:27017';
// Database Name---
const dbName = 'HeartRate';
//	Collection Name---
const My_collection = 'h1f001';



//3.findDocuments
const findDocuments = function(db, callback) {
  // Get the documents collection  你要插入的collection名稱。
  const collection = db.collection(My_collection);
  // Find some documents  找出所有資料
  collection.find({}).toArray(function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records");
    console.log(docs);
    callback(docs);
  });
}

//main---
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("server 連線成功");

  const db = client.db(dbName);
  //operations--
  findDocuments(db, function() {
      client.close();
    });
});
