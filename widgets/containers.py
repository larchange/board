from ..core import to_html, to_js
from ..core.widget import Widget
from collections.abc import MutableSequence


class Container(Widget, MutableSequence):
    def __init__(self, orient="vertical", max_per_row=6, *args, **kw):
        super().__init__(self, *args, **kw)
        self._content = []
        self.orient = orient
        assert max_per_row in (1, 2, 3, 4, 6, 12)
        self.max_per_row = max_per_row 

    async def render(self):
        response = await super().render()
        html = []
        js = []
        for number, widget in enumerate(self._content):
            res = await widget.render()
            if self.orient == "horizontal":
                html.append(
                    '<div class="col-md-{}">{}</div>'.format(
                        int(12 / self.max_per_row), 
                        res.html
                    )
                )
            else:
                html.append(
                    '<div>{}</div>'.format(res.html)
                )

            js.append(res.js)
            response.scripts |= res.scripts
            response.styles |= res.styles

        response.html = '<div id={} class="{}">{}</div>'.format(
            self.uuid,
            "row",
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

    def __lshift__(self, obj):
        self.append(obj)
    

