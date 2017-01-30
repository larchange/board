from board.widgets import containers
from board.widgets import graphs
from board.widgets import typography 
from board.core.plugin import Plugin
import numpy
import pandas


class DemoGraph(Plugin):
    title = "Graph"
    category = "Extra"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container.append(typography.Title("Simple graph", level=2))
        df = pandas.DataFrame(
            numpy.random.randn(100).cumsum(),
            columns=["random"]
        )
        container.append(graphs.Graph(df))
        container.append(typography.Title("Multiple graph", level=2))
        df = pandas.DataFrame(
            {
                'random': numpy.random.randn(100).cumsum(),
                'stillrandom': numpy.random.randn(100).cumsum()
            }
        )
        container.append(graphs.Graph(df))

        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())
        return container
