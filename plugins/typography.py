from board.widgets import containers
from board.widgets import typography
from board.core.plugin import Plugin


class DemoTypography(Plugin):
    title = "Typography"
    category = "Typo & contents"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container << typography.Title('Level 1 Title', level=1)
        container << typography.Title('Level 2 Title', level=2)

        hstack = containers.Container(orient="horizontal", max_per_row=2)
        hstack << typography.Blockquote(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'Someone famous',
            'Source Title'
        )
        hstack << typography.List(
            ['Hello', 'Buenos dia', 'Salut']
        )
        container << hstack
        container << (typography.Title('Some labels', level=2))

        hstack = containers.Container(orient="horizontal", max_per_row=2)
        hstack << typography.Label("Default", "default")
        hstack << typography.Label("Primary", "primary")
        hstack << typography.Label("Success", "success")
        hstack << typography.Label("Info", "info")
        hstack << typography.Label("Warning", "warning")
        hstack << typography.Label("Danger", "danger")
        container << hstack
        
        container << typography.Title("The source", level=2)
        container << code.MySource()

        return container
