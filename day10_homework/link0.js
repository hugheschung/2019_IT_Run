//1.link mongodb

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');

// 連接你的 mlab URL 記得要填上帳號密碼，是新增user時候的帳號密碼，別弄錯了。 
const url = 'mongodb://你的帳號:你的密碼.......';
// 記得<>要拿走....

// 你的DB名稱  
const dbName = '你的DB名稱';

//main--主程式區
//連接mlab mongoDB server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  
   //注意這一行，最後連線成功，cmd模式會輸出 
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  client.close();
});
