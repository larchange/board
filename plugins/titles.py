from board.widgets import containers
from board.widgets import titles
from board.core.plugin import Plugin


class DemoTitles(Plugin):
    title = "Title"
    category = "Demo titles and contents"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container.append(titles.Title('Level 1 Title', level=1))
        container.append(titles.Title('Level 2 Title', level=2))
        container.append(titles.Title('Level 3 Title', level=3))
        container.append(titles.Title('Level 4 Title', level=4))
        return container
