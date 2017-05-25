import os

os.environ.pop('GEVENT_LOOP', None)
from ws4py.websocket import WebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
import json
import CardReader
available_commands = ["add_player", "get", "set", "update"]


class MyWebSocket(WebSocket):
    def opened(self):
        print "Socket opened"

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
CardReader.reader()

