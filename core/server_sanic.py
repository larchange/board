import pandas
from jinja2 import Environment, FileSystemLoader
from . import plugin
from . import widget
from . import to_html
from . import to_js
import os
from ..plugins import demo
from collections import defaultdict
from sanic import Sanic
from sanic.response import text
from sanic.response import html



SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


ENV = Environment(
    loader=FileSystemLoader(SCRIPT_DIR + '/../templates'),
)

plugins = plugin.Plugin.plugins.values()
PLUGIN_BY_CAT = defaultdict(list)
for plug in plugins:
    if plug.category != "NOT_TO_DISPLAY_CAT":
        PLUGIN_BY_CAT[plug.category].append(plug)
PLUGIN_BY_CAT = dict(PLUGIN_BY_CAT)

app = Sanic(__name__)


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
    response = plug.init_page(
        **{
            key: value[0]
            for key, value in request.args.items()
        }
    )
    if plug.template:
        return html(ENV.get_template(plug.template).render(
            plugin=plug,
            plugin_content=to_html(response),
            plugin_js=to_js(response),
            scripts=widget.Widget.scripts,
            styles=widget.Widget.styles,
            plugins=PLUGIN_BY_CAT
        ))
    else:
        return html(to_html(response))

def start_server():
    app.run(host="0.0.0.0", port=8000, debug=True)