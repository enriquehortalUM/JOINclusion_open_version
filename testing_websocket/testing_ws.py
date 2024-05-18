# Author: Annanda Sousa (annanda.sousa@gmail.com)
import websocket
import json

ws = websocket.WebSocket()
ws.connect("ws://localhost:8080")
data = {
    'type': 'createRoom',
    'maxPlayers': 2,
    'gemForWSList': []
}
ws.send(json.dumps(data))

# print(ws.recv())
# ws.close()

# def on_message(wsapp, message):
#     print(message)
#
#
# wsapp = websocket.WebSocketApp("ws://localhost:8080", on_message=on_message)
# wsapp.run_forever()
#
# wsapp.send(json.dumps(data))
