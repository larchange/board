from ..core.widget import Jinja2Widget
from ..core import producer



class ProgressBar(Jinja2Widget, template="progression"):
    scripts = []

    def __init__(self, progression, init_value=0, *args, **kw):
        super().__init__(*args, **kw)
        self.progression = progression
        self.init_value = init_value

    async def data(self):
        producer.producer_registered[self.uuid] = self.progression

        return {
            'uuid': self.uuid,
            'value': self.init_value
        }

