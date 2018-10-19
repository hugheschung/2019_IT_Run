//day11 練習0: link mongodb

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


const url = 'mongodb://localhost:27017';


// 填入你的DB名稱  
const dbName = 'HeartRate';

//main--主程式區
//連接mlab mongoDB server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  
   //注意這一行，最後連線成功，cmd模式會輸出 
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  client.close();
});
