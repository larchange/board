from board.widgets import containers
from board.widgets import form
from board.core.plugin import Plugin


class DemoForm(Plugin):
    title = "Form"
    category = "Form"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()
        myform = form.Form()
        myform.append(form.Email("email"))
        myform.append(form.Password("passwd"))
        container.append(myform)
        container.append(typography.Title("The source", level=2))
        container.append(code.MySource())
        return container
