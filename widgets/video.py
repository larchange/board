from ..core.widget import Widget



class Youtube(Widget):
    def __init__(self, video_id, autoplay=False, start=0, ratio="16by9"):
        self.video_id = video_id
        self.autoplay = '1' if autoplay else '0'
        self.start = start
        self.ratio = ratio

    async def render(self):
        response = await super().render()
        response.html += '''
        <div class="embed-responsive embed-responsive-{ratio}"> 
        <iframe class="embed-responsive-item"
            src="https://www.youtube.com/embed/{video_id}?t={start}&autoplay={autoplay}"
            allowfullscreen></iframe></div>'''.format(**vars(self))
        return response


class Dailymotion(Widget):
    def __init__(self, video_id, ratio="16by9"):
        self.video_id = video_id
        self.ratio = ratio
        
    async def render(self):
        response = await super().render()
        response.html += """
            <div class="embed-responsive embed-responsive-{ratio}"> 
            <iframe class="embed-responsive-item"
            src="//www.dailymotion.com/embed/video/{video_id}"
            allowfullscreen></iframe></div>
        """.format(**vars(self))
        return response
