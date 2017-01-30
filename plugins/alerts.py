from board.widgets import containers
from board.widgets import alerts
from board.core.plugin import Plugin


class DemoAlert(Plugin):
    title = "Alerts"
    category = "Typo & contents"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container.append(
            alerts.Alert(
                "This alert needs your attention, but it's not super important."
            )
        )
        container.append(
            alerts.Alert(
                "Better check yourself, you're not looking too good.",
                kind="warning",
                dismissible=True
            )
        )

        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())

        return container
