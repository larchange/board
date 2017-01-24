from ..core.plugin import Plugin
from collections.abc import Mapping
import uuid


class FunctionRegister(Plugin, Mapping):
    title = "Function register"
    category = "NOT_TO_DISPLAY_CAT"
    template = None
   
    def __init__(self):
        self._container = {}

    def register(self, function):
        key = str(uuid.uuid1())
        self._container[key] = function
        return "/plugin/{}?uuid={}".format(
            self.__class__.__name__,
            key
        )

    def __getitem__(self, uuid):
        return self._container[uuid]
    
    def __iter__(self):
        return iter(self._container)
    
    def __len__(self):
        return len(self._container)

    async def init_page(self, uuid, **kw):
        return await self._container[uuid](**kw)

