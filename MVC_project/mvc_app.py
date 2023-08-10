import sys, os
from PyQt5.QtWidgets import QApplication
from model.model import Model
from controllers.main_ctrl import MainController
from views.main_view import MainView
import qdarktheme

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Connect everything together
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()
        self.main_ctrl.set_horns_mode()

if __name__ == '__main__':

    # At this point we may be running as root or as another user
    # - Check the parameters are valid - show an error if not
    # - Show the help message if requested
    # Don't do any work or anything time-consuming here as it will run twice

    if os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra "sudo" in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
        os.execvp("sudo", ["sudo"] + sys.argv)
    app = App(sys.argv)
    qdarktheme.setup_theme()
    sys.exit(app.exec_())