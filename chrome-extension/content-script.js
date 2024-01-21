const webSocket = new WebSocket('ws://localhost:12345/');

webSocket.onopen = function() {
    console.log('Connection opened');

    webSocket.onmessage = function(message) {
        console.log(message.data);
        if (message.data == "boba3") {
            console.log("we are scrolling");
            window.scrollBy(0, 100)
        }
    }
}