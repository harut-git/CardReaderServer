import json
import os
os.environ.pop('GEVENT_LOOP', None)

from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from ws4py.websocket import WebSocket


available_commands = ["add_employee", "update_employee", "get_employees", "get_logs", "listen_reader"]


class MyWebSocket(WebSocket):
    read_id = None

    def opened(self):
        print "Connection opened"

    def closed(self, code, reason=None):
        print "Hellloooo"

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


server = WSGIServer(('0.0.0.0', 8787), WebSocketWSGIApplication(handler_cls=MyWebSocket))
server.serve_forever()
