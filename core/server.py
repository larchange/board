import cherrypy
import pandas
from jinja2 import Environment, FileSystemLoader
from . import plugin
from . import widget
from . import to_html
from . import to_js
import os
from ..plugins import demo
from collections import defaultdict


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


class Web(object):
    @cherrypy.expose
    def index(self):
        scripts = widget.Widget.scripts
        styles = widget.Widget.styles

        return ENV.get_template("home.html").render(
            plugins=PLUGIN_BY_CAT,
            scripts=scripts
        )

    @cherrypy.expose
    def plugin(self, plugin_name, **kw):
        plug = plugin.Plugin.plugins[plugin_name]
        response = plug.init_page(**kw)
        if plug.template:
            return ENV.get_template(plug.template).render(
                plugin=plug,
                plugin_content=to_html(response),
                plugin_js=to_js(response),
                scripts=widget.Widget.scripts,
                styles=widget.Widget.styles,
                plugins=PLUGIN_BY_CAT
            )
        else:
            return to_html(response)



def start_server():
    conf = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8000,
        },
        '/': {
            'tools.sessions.on': True,
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': SCRIPT_DIR + '/../static'
        }
    }
    cherrypy.quickstart(Web(), '/', conf)
