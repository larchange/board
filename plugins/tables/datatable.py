from board.widgets import containers
from board.widgets import tables
from board.core.plugin import Plugin

import pandas
import statsmodels.api as sm


class DemoDataTable(Plugin):
    title = "DataTable"
    category = "Demo tables"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        self.df = sm.datasets.get_rdataset("Duncan", "car")
        container = containers.Container()
        container.append(tables.DataTable(self.df.data))
        return container
