import curses
from view import Menu, Content
from view import CurseView
from model import TaskList, TaskAPI


class PyTaskApp:

    def __init__(self):
        self.tsk_api = TaskAPI()
        self.tsk_api.connect()
        self.tasklists = self.tsk_api.get_taskslists()
        self.view = CurseView(self.tasklists)

    def application(self):
        while True:
            c = self.view.stdscr.getch()
            if c == ord('q'):
                self.view.quit()
                break
            elif c == ord('k') or c == ord('j'):
                self.view.move(c)
            elif c == ord('\t'):
                self.view.switch_window(c)
            elif c == ord('h') or c == ord('l'):
                self.view.switch_window(c)



PyTaskApp().application()
