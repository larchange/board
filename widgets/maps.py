from ..core.widget import Jinja2Widget
from ..core import producer
from board import dependancies


class Map(Jinja2Widget, template="map"):
    scripts = [dependancies.scripts.openlayers]
    styles = [dependancies.styles.openlayers]

    def __init__(self, longitude, latitude, zoom=4, *args, **kw):
        super().__init__(*args, **kw)
        self.longitude = longitude
        self.latitude = latitude
        self.zoom = zoom

    async def data(self):
        return vars(self)

