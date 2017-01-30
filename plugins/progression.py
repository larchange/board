import asyncio
import random
from board.widgets import containers
from board.widgets import progress
from board.widgets import typography
from board.widgets import code
from board.core.plugin import Plugin


class DemoProgressBar(Plugin):
    title = "ProgressBar"
    category = "Websocket"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container.append(typography.Paragraph(
            "This below progressbar websocket"
            " connected to a python async producer!"
        ))
        container.append(progress.ProgressBar(progress_producer))
        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())
        return container


async def progress_producer():
    percentage = 0
    while percentage <= 100:
        yield percentage
        percentage += random.choice([-1, 0, 1, 2])
        percentage = max(0, percentage)
        await asyncio.sleep(random.random())
