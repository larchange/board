


class Plugin:

    plugins = {}
    template = "plugin.html"

    def __init_subclass__(cls):
        Plugin.plugins[cls.__name__] = cls()

    def init_page(self, **kw):
        return "Base plugin"

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name
