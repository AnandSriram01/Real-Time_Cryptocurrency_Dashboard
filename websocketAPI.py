import websocket, json

ws_sendData = websocket.WebSocket()
ws_sendData.connect('ws://localhost:8000/ws/polData/')
# ws_sendData.send("message")

def on_message(ws, message):
    print("On Message")
    ws_sendData.send(message)
    current_tick = json.loads(message)
    print(current_tick['product_id'], " : ", current_tick['price'])

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("On Close")

def on_open(ws):
    print("On Open")

    subscribe_message = {
        "type": "subscribe",

        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "BTC-USD",
                    "ETH-USD"
                ]
            }
        ]
    }

    ws.send(json.dumps(subscribe_message))


socket_url = "wss://ws-feed.pro.coinbase.com"

ws_getData = websocket.WebSocketApp(socket_url,
                          on_open = on_open,
                          on_message = on_message,
                          on_error = on_error,
                          on_close = on_close)

ws_getData.run_forever()
