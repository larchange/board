from board.widgets import containers
from board.widgets import time
from board.widgets import typography
from board.core.plugin import Plugin


class DemoTimeWithWS(Plugin):
    title = "Time with websocket"
    category = "Websocket"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container.append(typography.Paragraph(
            "This below time is a websocket"
            " connected to a python async producer!"
        ))
        container.append(time.Time())
        return container
