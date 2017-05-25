import os

os.environ.pop('GEVENT_LOOP', None)
from ws4py.websocket import WebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
import json
import CardReader

available_commands = ["add_player", "get", "set", "update"]


class MyWebSocket(WebSocket):
    k = None

    def opened(self):
        while 1:
            self.k = CardReader.reader()
            if self.k == "in1222545":
                self.send("already -in")
            else:
                self.send("Enter a name" + self.k)

    def received_message(self, message):
        request = json.loads(str(message))
        command = request['command']
        params = request['params']
        if command not in available_commands:
            response = {
                "status": "false",
                "error": 3
            }
            self.send(json.dumps(response), message.is_binary)
        module = __import__('socket_commands')
        attr = getattr(module, command)
        response = attr(params=params)
        print "response: ", response
        self.send(json.dumps(response), message.is_binary)
        print self.environ


server = WSGIServer(('localhost', 8282), WebSocketWSGIApplication(handler_cls=MyWebSocket))
server.serve_forever()
