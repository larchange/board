from ..core.widget import Widget



class Youtube(Widget):
    def __init__(self, video_id, autoplay=False, start=0, width=560, height=315):
        self.video_id = video_id
        self.autoplay = '1' if autoplay else '0'
        self.start = start
        self.width = width
        self.height = height

    async def render(self):
        response = await super().render()
        response.html += ('<iframe width="{width}" height="{height}" '
            'src="https://www.youtube.com/embed/{video_id}'
            '?t={start}&autoplay={autoplay}" frameborder="0" '
            'allowfullscreen></iframe>').format(
                **vars(self)
        )
        return response


class Dailymotion(Widget):
    def __init__(self, video_id, width=560, height=315):
        self.video_id = video_id
        self.width = width
        self.height = height
        
    async def render(self):
        response = await super().render()
        response.html += """
            <iframe frameborder="0" width="{width}" height="{height}"
            src="//www.dailymotion.com/embed/video/{video_id}"
            allowfullscreen></iframe>
        """.format(**vars(self))
        return response
