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
        full_container = containers.Container()
        hstack = containers.Container(orient="horizontal", max_per_row=2)
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

        hstack << container

        container = containers.Container()
        container.append(typography.Title(
            "Rempaillage cannage prés des yvelines versailles houdan",
            level=2
        ))
        container.append(video.Dailymotion("xgshqb"))
        container.append(typography.Paragraph(
            "To go further: "
            "http://dailymotion.canalblog.com/archives/2011/02/10/20351553.html"
        ))

        hstack << container
        full_container << hstack
        full_container << typography.Title("The source", level=2)
        full_container << code.MySource()

        return full_container
