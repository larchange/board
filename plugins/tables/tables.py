from board.widgets import containers
from board.widgets import tables
from board.core.plugin import Plugin

import pandas
import statsmodels.api as sm


class DemoTable(Plugin):
    title = "Table"
    category = "Typo & contents"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        self.df = sm.datasets.get_rdataset("Duncan", "car")
        container = containers.Container()
        container.append(tables.Table(self.df.data))

        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())

        return container
