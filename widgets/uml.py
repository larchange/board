from ..core.widget import Widget
from board import dependancies


class Uml(Widget):
    scripts = [dependancies.scripts.mermaid]
    styles = [dependancies.styles.mermaid]

    def __init__(self, definition, *args, **kw):
        super().__init__(*args, **kw)
        self.definition = definition

    async def render(self):
        response = await super().render()
        response.html = '<div class="mermaid">{}</div>'.format(self.definition)
        response.uml = '''
            <script>mermaid.initialize({startOnLoad:true});</script>
        '''
        return response
