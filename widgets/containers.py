from ..core import to_html, to_js
from ..core.widget import Widget
from collections.abc import MutableSequence


class Container(Widget, MutableSequence):
    def __init__(self, orient="vertical", *args, **kw):
        super().__init__(self, *args, **kw)
        self._content = []
        self.orient = orient

    async def render(self):
        response = await super().render()
        html = []
        js = []
        for widget in self._content:
            res = await widget.render()
            html.append(res.html)
            js.append(res.js)
            response.scripts |= res.scripts
            response.styles |= res.styles

        response.html = "<div id={}>{}<div>".format(
            self.uuid,
            "".join(html)
        )

        response.js = "".join(js)
        return response

    def __getitem__(self, idx):
        self._content[idx]

    def __setitem__(self, idx, obj):
        self._content[idx] = obj

    def __delitem__(self, idx):
        del self._content[idx]

    def __len__(self):
        return len(self._content)

    def insert(self, idx, obj):
        self._content.insert(idx, obj)
