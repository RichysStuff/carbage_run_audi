import sys, os
from PyQt5.QtWidgets import QApplication
from model.model import Model
from controllers.main_ctrl import MainController
from views.main_view import MainView
import qdarktheme
import os

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
    print('cwd ', os.getcwd())
    app = App(sys.argv)
    qdarktheme.setup_theme()
    sys.exit(app.exec_())
