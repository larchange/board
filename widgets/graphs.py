from ..core.widget import Jinja2Widget
from board.core.plugin import Plugin


class Graph(Jinja2Widget, template="graph"):
    scripts = [
        "http://dygraphs.com/2.0.0/dygraph.min.js",
    ]
    styles = ["http://dygraphs.com/2.0.0/dygraph.css"]

    def __init__(self, df, *args, **kw):
        super().__init__(*args, **kw)
        self.df = df
        self.data_url = Plugin.plugins["FunctionRegister"].register(self.csv_graph)

    async def data(self):
        return {
            'uuid': self.uuid,
            'data_url': self.data_url
        }

    async def csv_graph(self, **kw):
        return self.df.to_csv()
