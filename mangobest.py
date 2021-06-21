from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText

def mango(screen):
    effects = [
        Cycle(
            screen,
            FigletText("MANGOS ARE", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("BEST!", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(mango)
