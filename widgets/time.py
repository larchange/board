import asyncio
from ..core.widget import Jinja2Widget
from ..core.plugin import Plugin
from ..core import producer
import datetime


class Time(Jinja2Widget, template="time"):
    scripts = []

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    async def data(self):
        producer.producer_registered[self.uuid] = self.current_date

        return {
            'uuid': self.uuid,
        }

    async def current_date(self, websocket):
        try:
            while True:
                now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                await websocket.send(now)
                await asyncio.sleep(1)
        except:
            print("Connection with %s closed" % websocket)
