from ..core.widget import Jinja2Widget
from ..core.plugin import Plugin
import numpy as np


class Table(Jinja2Widget, template="tables"):
    scripts = []

    def __init__(self, df, *args, **kw):
        super().__init__(*args, **kw)
        self.df = df

    def data(self):
        return {
            'uuid': self.uuid,
            'columns': self.df.columns,
            'values': self.df.values
        }


class DataTable(Jinja2Widget, template="datatable"):
    scripts = [
        "https://cdn.datatables.net/1.10.13/js/jquery.dataTables.min.js",
    ]
    styles = ["https://cdn.datatables.net/1.10.13/css/jquery.dataTables.min.css"]

    def __init__(self, df, *args, **kw):
        super().__init__(*args, **kw)
        self.df = df
        self.data_url = Plugin.plugins["FunctionRegister"].register(self.chunk)

    def data(self):
        return {
            'uuid': self.uuid,
            'columns': self.df.columns,
            'data_url': self.data_url
        }

    def chunk(self, draw, start, length, **kw):
        start = int(start)
        length = int(length)
        column_order = int(kw.get('order[0][column]'))
        ascending = kw.get("order[0][dir]") == "asc"
        
        df = self.df.sort_values(
            by=self.df.columns[column_order],
            ascending=ascending
        )

        search = kw.get("search[value]")
        if search:
            mask = np.column_stack([
                df[col].astype(str).str.contains(search, na=False) for col in df
            ])
            df = df.loc[mask.any(axis=1)]

        return '''{
            "draw": %s,
            "recordsTotal": %s,
            "recordsFiltered": %s,
            "data": %s
            }''' % (
                draw,
                len(self.df),
                len(df),
                df.iloc[start:min(len(df), start + length)].to_json(orient="values")
            )
