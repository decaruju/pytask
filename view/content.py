import curses


class Content:

    def __init__(self, tasks):
        self._window = curses.newwin(curses.LINES-1, curses.COLS-20, 0, 20)
        self._window.box()
        self.tasks = tasks
        self.curs_pos = 0

        self.redraw(0)

    def redraw(self, index):
        self._window.clear()
        self._window.box()
        for i, task in enumerate(self.tasks):
            task.set_pos(i+1, 1)
            if i == index:
                self.addstr(*task.addstr(), curses.A_REVERSE)
                self.current_task= task
            else:
                self.addstr(*task.addstr())

        self.noutrefresh()
        curses.doupdate()

    def __getattr__(self, attr_name):
        return getattr(self._window, attr_name)
