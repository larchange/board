from board.widgets import containers
from board.widgets import tables
from board.core.plugin import Plugin

import pandas


class DemoDataTable(Plugin):
    title = "DataTable"
    category = "Typo & contents"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        self.df = pandas.DataFrame({
            "a": [1, 2, 3, 4],
            "b": ["q", "w", "q", "w"]
        })
        container = containers.Container()
        container.append(tables.DataTable(self.df))

        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())

        return container
