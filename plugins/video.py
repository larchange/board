from board.widgets import containers
from board.widgets import video
from board.widgets import typography
from board.core.plugin import Plugin
import inspect


class DemoEmbeddedVideo(Plugin):
    title = "Embedded video"
    category = "Extra"

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

        container.append(typography.Title(
            "Rempaillage cannage prés des yvelines versailles houdan",
            level=2
        ))
        container.append(video.Dailymotion("xgshqb"))
        container.append(typography.Paragraph(
            "To go further: "
            "http://dailymotion.canalblog.com/archives/2011/02/10/20351553.html"
        ))


        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())
        return container
