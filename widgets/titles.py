from ..core.widget import Widget


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
