import os
import sys

print sys.version_info
os.environ.pop('GEVENT_LOOP', None)

from gevent.wsgi import WSGIServer
import json

available_modules = ["check", "get", "set", "update"]
available_methods = ["login", "token", "email", "files", "registration", "download", "new_folder", "new_player"]
available_commands = ["listen_reader"]


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # start_response('200 OK', [('Access-Control-Allow-Origin','*')])
    request = json.loads(environ['wsgi.input'].read())
    print "request:", request
    command = request['command']
    params = request['params']
    if command not in available_commands:
        response = {
            "status": "false",
            "error": 3
        }
        return json.dumps(response)

    module = __import__('socket_commands')
    attr = getattr(module, command)
    response = attr(params=params)
    print "response: ", response
    return json.dumps(response)


print 12313
WSGIServer(('', 9092), application).serve_forever()
