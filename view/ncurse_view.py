from view import Content, Menu, BottomText
from enum import Enum
import curses

class UI_ELEMENT(Enum):
    menu = 1
    content = 2

class CurseView:

    def __init__(self, tasklists):
        curses.wrapper(self._init_curse)

        self.stdscr.noutrefresh()
        self.menu = Menu(tasklists)
        self.content = Content(tasklists[0].tasks)
        self.btext = BottomText()
        self.is_cursor_on_menu = True

        curses.doupdate()

    def _init_curse(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.nodelay(True)
        self.stdscr.clear()
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        if curses.has_colors:
            curses.start_color()

    def move(self, c):
        if c == ord('k'):
            if self.is_cursor_on_menu:
                self.menu.move_up()
                self.content.tasks = self.menu.current_tasklist.tasks
                self.content.curs_pos = 0
                self.content.redraw(None)
            else:
                self.content.move_up()
        elif c == ord('j'):
            if self.is_cursor_on_menu:
                self.menu.move_down()
                self.content.tasks = self.menu.current_tasklist.tasks
                self.content.curs_pos = 0
                self.content.redraw(None)
            else:
                self.content.move_down()

        self.btext.redraw()


    def switch_window(self, c):
        self.is_cursor_on_menu = not self.is_cursor_on_menu
        if not self.is_cursor_on_menu:
            self.content.redraw(0)
        else:
            self.content.redraw(None)

        self.btext.redraw()

    def start_loop():
        stdscr.noutrefresh()
        curses.doupdate()

    def quit(self):
        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        curses.endwin()
