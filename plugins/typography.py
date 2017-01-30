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
        container.append(typography.Title('Level 1 Title', level=1))
        container.append(typography.Title('Level 2 Title', level=2))
        container.append(
            typography.Blockquote(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                'Someone famous',
                'Source Title'
            )
        )
        container.append(typography.Title('Level 2 Title', level=2))
        container.append(typography.List(
                ['Hello', 'Buenos dia', 'Salut']
            )
        )
        container.append(typography.Title('Some labels', level=2))

        container.append(typography.Label("Default", "default"))
        container.append(typography.Label("Primary", "primary"))
        container.append(typography.Label("Success", "success"))
        container.append(typography.Label("Info", "info"))
        container.append(typography.Label("Warning", "warning"))
        container.append(typography.Label("Danger", "danger"))
        
        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())

        return container
