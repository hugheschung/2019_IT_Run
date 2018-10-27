

	//建立websocket連線
	url="ws:localhost:8888/ws"
	ws = new WebSocket(url)

	//確認連線用指令
	ws.readyState
	//或是
	ws.OPEN

	
	//定義websocket連線
	url="ws:localhost:8888/ws" ;
    ws = new WebSocket(url);
	
	//定義:連線開啟時的動作
    ws.onopen = function() {
      var x = "hello,這是黑修斯在day19寫的測試頁" ;
      ws.send(x);
    };
	
	//定義:有訊息進來時的動作
    ws.onmessage = function (evt) {
      xx = evt.data  //外部變數xx,用於調試檢查內容
      console.log(xx);
       alert(evt.data);
    };
	
	//定義:連線中斷時的動作
    ws.onclose=function(){
      alert("斷線了");
    };
	
	//傳送訊息使用
	ws.send()