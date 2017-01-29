from board.widgets import containers
from board.widgets import video
from board.widgets import typography
from board.core.plugin import Plugin


class DemoEmbeddedVideo(Plugin):
    title = "Embedded video"
    category = "Video"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        container.append(typography.Title(
            "Thinking about Concurrency, Raymond Hettinger",
            level=2
        ))
        container.append(video.Youtube("Bv25Dwe84g0"))
        container.append(typography.Paragraph(
            "To go further: "
            "https://developers.google.com/youtube/iframe_api_reference"
        ))
        return container
