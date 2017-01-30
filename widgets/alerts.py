from ..core.widget import Jinja2Widget
from board import dependancies


class Alert(Jinja2Widget, template='alert'):
    def __init__(self, content, kind="info", dismissible=False):
        self.content = content
        self.kind = kind
        self.dismissible = dismissible

    async def data(self):
        return vars(self)
