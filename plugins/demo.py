from ..widgets import containers
from ..widgets import titles
from ..widgets import tables
from ..core.plugin import Plugin

import pandas
import statsmodels.api as sm


class Demo(Plugin):
    title = "Demo"
    category = "Demo category"

    def __init__(self):
        super().__init__()
        self.df = sm.datasets.get_rdataset("Duncan", "car")

    def init_page(self, **kw):
        container = containers.Container()
        container.append(tables.DataTable(self.df.data))
        return container
