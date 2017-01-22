from ..core import to_html, to_js
from ..core.widget import Widget
from collections.abc import MutableSequence


class Container(Widget, MutableSequence):
    def __init__(self, orient="vertical", *args, **kw):
        super().__init__(self, *args, **kw)
        self._content = []
        self.orient = orient

    def render_html(self):
        return "<div id={}>{}<div>".format(
            self.uuid,
            "".join(map(to_html, self._content))
        )

    def render_js(self):
        return "".join(map(to_js, self._content))

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
