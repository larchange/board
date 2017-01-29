import inspect, os
from ..core.widget import Widget
from board import dependancies


class Code(Widget):
    scripts = [
        dependancies.scripts.highlight
    ]
    styles = [
        dependancies.styles.highlight
    ]

    def __init__(self, code, language="nohighlight"):
        self.code = code
        self.language = language

    async def render(self):
        response = await super().render()
        response.html += '''
            <pre><code class="{language}">{code}</code></pre>
        '''.format(
            code=self.code,
            language=self.language
        )
        response.js += "<script>hljs.initHighlightingOnLoad();</script>"
        return response


class SourcePython(Code):
    def __init__(self, filename):
        self.filename = filename
        code = open(filename).read()
        super().__init__(code=code, language="python")


class MySource(SourcePython):
    def __init__(self):
        frame = inspect.currentframe()
        outerframes = inspect.getouterframes(frame)
        filename = inspect.getfile(outerframes[1].frame)
        super().__init__(filename)
