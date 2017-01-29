from ..core.widget import Jinja2Widget
from ..core.widget import Widget
from ..core.plugin import Plugin
import numpy as np


class Blockquote(Jinja2Widget, template="blockquote"):
    scripts = []

    def __init__(self, quote, small=None, source=None, *args, **kw):
        super().__init__(*args, **kw)
        self.quote = quote
        self.small = small
        self.source = source

    async def data(self):
        return {
            'uuid': self.uuid,
            'quote': self.quote,
            'small': self.small,
            'source': self.source
        }


class List(Jinja2Widget, template="list"):
    scripts = []

    def __init__(self, elements, kind='unordered', *args, **kw):
        super().__init__(*args, **kw)
        self.elements = elements

    async def data(self):
        return {
            'uuid': self.uuid,
            'elements': self.elements,
        }


class Title(Widget):
    def __init__(self, title, level=1):
        self.level = level
        self.title = title

    async def render(self):
        response = await super().render()
        response.html += '<h{level}>{title}</h{level}>'.format(
            level=self.level,
            title=self.title
        )
        return response


class Paragraph(Widget):
    def __init__(self, text):
        self.text = text

    async def render(self):
        response = await super().render()
        response.html += '<p>{}</p>'.format(
            self.text
        )
        return response
