from ..core.widget import Widget


class Title(Widget):
    def __init__(self, title, level=1):
        self.level = level
        self.title = title

    def render_html(self):
        return '<h{level}>{title}</h{level}>'.format(
            level=self.level,
            title=self.title
        )
