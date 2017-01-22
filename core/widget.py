import os
import uuid
from jinja2 import Environment, FileSystemLoader
import functools


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


class Widget:
    """Base class for Widgets"""

    scripts = set()
    styles = set()

    def __new__(cls, *args, **kw):
        instance = super().__new__(cls)
        Widget.scripts |= set(cls.scripts)
        Widget.styles |= set(cls.styles)
        return instance

    def __init__(self, *args, **kw):
        super().__init__()
        self.uuid = "id_{}".format(uuid.uuid1())

    def render_html(self):
        pass

    def render_js(self):
        return ""
 

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

    def render_html(self):
        self.data_cache = self.data()
        return self.template.render(**self.data_cache)

    def render_js(self):
        if self.template_js is not None:
            res = self.template_js.render(**self.data_cache)
            self.data_cache = None
            return res
        else:
            return ""

    def data(self):
        return {}
