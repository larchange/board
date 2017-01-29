from ..core import to_html, to_js
from ..core.widget import Widget
from collections.abc import MutableSequence




class Form(Widget, MutableSequence):
    def __init__(self, *args, **kw):
        super().__init__(self, *args, **kw)
        self._content = []

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

        response.html = "<form id={}>{}</form>".format(
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


class Email(Widget):
    def __init__(self, form_id, label="Email", placeholder="Email"):
        self.form_id = form_id
        self.label = label
        self.placeholder = placeholder

    async def render(self):
        response = await super().render()
        response.html += '''
            <div class="form-group">
                <label for="{form_id}">{label}</label>
                <input type="email"
                       class="form-control"
                       id="{form_id}"
                       placeholder="{placeholder}"
                >
            </div>
        '''.format(**vars(self))

        return response


class Password(Widget):
    def __init__(self, form_id, label="Password", placeholder="Password"):
        self.form_id = form_id
        self.label = label
        self.placeholder = placeholder

    async def render(self):
        response = await super().render()
        response.html += '''
            <div class="form-group">
                <label for="{form_id}">{label}</label>
                <input type="password"
                       class="form-control"
                       id="{form_id}"
                       placeholder="{placeholder}"
                >
            </div>
        '''.format(**vars(self))

        return response


class Input(Widget):
    def __init__(self, form_id, label="Password", placeholder="Password"):
        self.form_id = form_id
        self.label = label
        self.placeholder = placeholder

    async def render(self):
        response = await super().render()
        response.html += '''
            <div class="form-group">
                <label for="{form_id}">{label}</label>
                <input type="password"
                       class="form-control"
                       id="{form_id}"
                       placeholder="{placeholder}"
                >
            </div>
        '''.format(**vars(self))

        return response
