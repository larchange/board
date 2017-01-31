from board.widgets import containers
from board.widgets import typography
from board.widgets.uml import Uml
from board.core.plugin import Plugin


class DemoUml(Plugin):
    title = "Uml"
    category = "Extra"

    def __init__(self):
        super().__init__()

    async def init_page(self, **kw):
        container = containers.Container()

        container << typography.Title("Graph LR")
        container << Uml('''
            %% Example diagram
            graph LR
                A[Square Rect] -- Link text --> B((Circle))
                A --> C(Round Rect)
                B --> D{Rhombus}
                C --> D
        ''')


        container << typography.Title("Sequence diagram")
        container << Uml('''
        %% Sequence diagram code
        sequenceDiagram
            Alice ->> Bob: Hello Bob, how are you?
            Bob-->>John: How about you John?
            Bob--x Alice: I am good thanks!
            Bob-x John: I am good thanks!
            Note right of John: Bob thinks a long.

            Bob-->Alice: Checking with John...
            Alice->John: Yes... John, how are you?
        ''')

        container << Uml('''
            %% Sequence diagram code
            sequenceDiagram
                loop Daily query
                    Alice->>Bob: Hello Bob, how are you?
                    alt is sick
                        Bob->>Alice: Not so good :(
                    else is well
                        Bob->>Alice: Feeling fresh like a daisy
                    end

                    opt Extra response
                        Bob->>Alice: Thanks for asking
                    end
                end
        ''')

        container << typography.Title("The source", level=2)
        container << code.MySource()

        return container


