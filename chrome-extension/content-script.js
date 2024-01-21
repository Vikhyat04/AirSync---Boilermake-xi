const webSocket = new WebSocket('ws://localhost:12345/');

webSocket.onopen = function() {
    console.log('Connection opened');

    webSocket.onmessage = function(message) {
        let { data } = message;
        console.log(data)
        if (data == "1") {
            history.back()
        }
        else if (data == "2") {
            history.forward()
        }
        else if (data == "4") {
            window.scrollBy({top: 400, behavior: "smooth"})
        }
        else if (data == "3") {
            window.scrollBy({top: -400, behavior: "smooth"})
        }
    }
}