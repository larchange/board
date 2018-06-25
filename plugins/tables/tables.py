from board.widgets import containers
from board.widgets import tables
from board.core.plugin import Plugin

import pandas


class DemoTable(Plugin):
    title = "Table"
    category = "Typo & contents"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        self.df = pandas.DataFrame({
            "a": [1, 2, 3, 4],
            "b": [2, 3, 4, 5]
        })
        container = containers.Container()
        container.append(tables.Table(self.df))

        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())

        return container
