from gevent.wsgi import WSGIServer
import json

available_modules = ["check", "get", "set", "update"]
available_methods = ["login", "token", "email", "files", "registration", "download", "new_folder", "new_player"]
players_list = []


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # start_response('200 OK', [('Access-Control-Allow-Origin','*')])
    request = json.loads(environ['wsgi.input'].read())
    print "request:", request
    command = request['command']
    what = request['what']
    params = request['params']

    if command not in available_modules or what not in available_methods:
        response = {
            "status": "false",
            "error": 3
        }
        return json.dumps(response)

    module = __import__(command)
    attr = getattr(module, what)
    response = attr(params=params)

    print "response: ", response
    return json.dumps(response)


WSGIServer(('', 8000), application).serve_forever()
