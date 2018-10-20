//day12 練習2: insert some documents + findDocuments
//1.link mongodb	連結mongoDB
//2.insertDocuments	插入指令
//3.findDocuments  查找資料指令

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL---
const url = 'mongodb://localhost:27017';
// Database Name---
const dbName = 'HeartRate';


//2.insertDocuments  插入指令(day11中有做過的插入練習)
const insertDocuments = function(db, callback) {
  // Get the documents collection  你要插入的collection名稱。
  const collection = db.collection('h1f001');
  // Insert some documents
  collection.insertMany([
    {day9 : 1}, {day10 : 2}, {day11 : 3}
  ], function(err, result) {
    assert.equal(err, null);
    //assert.equal(3, result.result.n);	//可以註解
    //assert.equal(3, result.ops.length); //可以註解
    console.log("已經插入"+ result.result.n +"筆資料到collection");
    callback(result);
  });
}

//3.findDocuments 查找資料指令
const findDocuments = function(db, callback) {
  // Get the documents collection  你要查詢的collection名稱
  const collection = db.collection('h1f001');
  // Find some documents
  collection.find({}).toArray(function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records : 找到的資料如下");
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
  insertDocuments(db, function() {
    findDocuments(db, function() {
      client.close();
    });
  });
});
