import json
import re

import serial
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from ws4py.websocket import WebSocket

import CardReader
from socket_commands import check_if_emp_exists

available_commands = ["add_employee", "update_employee", "get_employees", "get_logs"]


class MyWebSocket(WebSocket):
    read_id = None

    def opened(self):
        print "Connection opened"

    def closed(self, code, reason=None):
        print "Hellloooo"

    def received_message(self, message):
        print message
        if str(message) == "enable_reader":
            ser = serial.Serial(port='COM1', baudrate='9600')
            k = CardReader.reader(ser)
            ser.close()
            print "port closed"
            self.read_id = k
            self.read_id = re.sub('[a-z]', '', self.read_id)
            print self.read_id
            if not check_if_emp_exists(self.read_id):
                response = {'command': "add_employee",
                            'params': {
                                'entry_id': self.read_id
                            }}
                self.send(json.dumps(response))
            else:
                self.send(json.dumps({'command': "employee_exists",
                                      'params': {
                                          'entry_id': self.read_id
                                      }}))
        else:
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


server = WSGIServer(('0.0.0.0', 8989), WebSocketWSGIApplication(handler_cls=MyWebSocket))
server.serve_forever()
