from ..core.widget import Widget



class Youtube(Widget):
    def __init__(self, video_id, autoplay=False, start=0):
        self.video_id = video_id
        self.autoplay = '1' if autoplay else '0'
        self.start = start

    async def render(self):
        response = await super().render()
        response.html += ('<iframe width="560" height="315" '
            'src="https://www.youtube.com/embed/{video_id}'
            '?t={start}&autoplay={autoplay}" frameborder="0" '
            'allowfullscreen></iframe>').format(
            video_id=self.video_id,
            start=self.start,
            autoplay=self.autoplay
        )
        return response
