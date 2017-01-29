import pandas
from jinja2 import Environment, FileSystemLoader
from . import plugin
from . import widget
from . import to_html
from . import to_js
import os
from collections import defaultdict
from sanic import Sanic
from sanic.response import text
from sanic.response import html

import asyncio
import websockets
import uvloop
from . import producer

import logging
logger = logging.getLogger('websockets.server')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

app = Sanic(__name__)


ENV = Environment(
    loader=FileSystemLoader(SCRIPT_DIR + '/../templates'),
)

plugins = plugin.Plugin.plugins.values()
PLUGIN_BY_CAT = defaultdict(list)
for plug in plugins:
    if plug.category != "NOT_TO_DISPLAY_CAT":
        PLUGIN_BY_CAT[plug.category].append(plug)
PLUGIN_BY_CAT = dict(PLUGIN_BY_CAT)



@app.route("/")
async def handle_index(request):
    scripts = widget.Widget.scripts
    styles = widget.Widget.styles

    return html(ENV.get_template("home.html").render(
        plugins=PLUGIN_BY_CAT,
        scripts=scripts
    ))


@app.route("/plugin/<plugin_name>")
async def handle_plugin(request, plugin_name):
    plug = plugin.Plugin.plugins[plugin_name]
    response = await plug.init_page(
        **{
            key: value[0]
            for key, value in request.args.items()
        }
    )
    if plug.template:
        response = await response.render()
        return html(ENV.get_template(plug.template).render(
            plugin=plug,
            plugin_content=response.html,
            plugin_js=response.js,
            scripts=response.scripts,
            styles=response.styles,
            plugins=PLUGIN_BY_CAT
        ))
    else:
        return html(response)


async def ws(websocket, path):
    name = await websocket.recv()
    try:
        await producer.producer_registered.pop(name)(websocket)
    except:
        import traceback
        traceback.print_exc()


loop = asyncio.get_event_loop()
ws_server = websockets.serve(
    ws, '', 9000,
    loop=loop
)
loop.run_until_complete(ws_server)


def start_server():
    app.run(host="0.0.0.0", port=8000, debug=True, loop=loop)
