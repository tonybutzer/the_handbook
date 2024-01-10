from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.events import NewRequest
import json
import os
import logging

debug_level = logging.INFO
if "DEBUG_LEVEL" in os.environ:
  debug_level = logging.DEBUG if os.environ["DEBUG_LEVEL"] == "DEBUG" else logging.INFO

print("debug_level is: " + str(debug_level))


logger = logging.getLogger(__name__)
logger.setLevel(debug_level)

def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS,HEAD',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)


@view_config(renderer='json')
def hello_world(request):
    return {'ARD':'We got that!'}


@view_config(renderer='json', header={"Access-Control-Allow-Origin":"*"})
def get_tile(request):
    output = []
    tileid = request.matchdict['tileid']
    base_path = "/resources/ardtars/"

    # if this file isn't here, go home
    with open("ard_map.json", "r") as file:
        ard_map = json.loads(file.read())

    try:
        ard_paths = ard_map[tileid]
        for path in ard_paths:
            tardir = base_path + path
            try:
                for tar in os.listdir(tardir):
                    output.append(tar)
            except FileNotFoundError as e:
                logger.debug("Directory not found: %s" % tardir)
    except KeyError as e:
        logger.debug("Tile id not found in ard_map: " + tileid)

    return output

if __name__ == '__main__':
    config = Configurator(debug_logger=logger)
    config.add_route('hello', '/')
    config.add_route('get_tile', '/ard/{tileid}')
    config.add_view(hello_world, route_name='hello', renderer='json')
    config.add_view(get_tile, route_name='get_tile', renderer='json')
    config.add_static_view('ardtars', 'resources/ardtars', cache_max_age=3600, request_method=("HEAD", "GET"))
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
