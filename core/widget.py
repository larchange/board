import os
import uuid
from jinja2 import Environment, FileSystemLoader
import functools


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


class Response(object):
    def __init__(self):
        self.html = ""
        self.js = ""
        self.styles = set()
        self.scripts = set()


class Widget:
    """Base class for Widgets"""

    scripts = set()
    styles = set()

    def __init__(self, *args, **kw):
        super().__init__()
        self.uuid = "id_{}".format(uuid.uuid1())

    async def render(self):
        response = Response()
        response.scripts |= set(self.scripts)
        response.styles |= set(self.styles)
        return response
 

class Jinja2Widget(Widget):
    """Subclass of this base widget should override data method.
    data method should return a dictionary of the variable to render in the
    template
    """

    jinja_env = Environment(
        loader=FileSystemLoader(SCRIPT_DIR + '/../templates'),
    )

    def __init_subclass__(cls, template, **kw):
        super().__init_subclass__(**kw)
        cls.template = cls.jinja_env.get_template(template + '.html')
        try:
            cls.template_js = cls.jinja_env.get_template(template + '.js')
        except:
            cls.template_js = None

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.data_cache = None

    async def render(self):
        response = await super().render()
        data = await self.data()
        response.html += await self.render_html(data)
        response.js += await self.render_js(data)
        return response

    async def render_html(self, data):
        return self.template.render(**data)

    async def render_js(self, data):
        if self.template_js is not None:
            res = self.template_js.render(**data)
            return res
        else:
            return ""

    async def data(self):
        return {}
