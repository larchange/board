from board.widgets import containers
from board.widgets import maps
from board.widgets import typography 
from board.core.plugin import Plugin


class DemoMap(Plugin):
    title = "Map from OpenStreetMap"
    category = "Extra"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container.append(maps.Map(2.3, 48.9, zoom=8))

        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())
        return container
