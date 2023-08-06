from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from views.ui_Grid_gui import Ui_MainWindow


class MainView(QMainWindow):

    activated_color = '#b34700'
    disactivated_color = '#37414F'

    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect ui-widget to controller
        # if ui changes, it sends a signal to an slot on which we connect a controller class.
        # therefore we can recive the signal in the controller
        """ self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        # Lambda to execute function with value
        self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        self._ui.pushButton_add.clicked.connect(lambda: self._main_controller.add_user(self._ui.lineEdit_name.text()))
        self._ui.pushButton_delete.clicked.connect(lambda: self._main_controller.delete_user(self._ui.listWidget_names.currentRow())) """
        self.sCt_pB_horns_menu = QShortcut(u"0", self, self._main_controller.set_horns_mode)
        self.sCt_pB_lights_menu = QShortcut(u"1", self, self._main_controller.set_lights_mode)
        self.sCt_pB_speaker_menu = QShortcut(u"4", self, self._main_controller.set_speaker_mode)
        self.sCt_pB_settings_menu = QShortcut(u"7", self, self._main_controller.set_settings_mode)
        
        self.sCt_pB_1_0 = QShortcut(u"2", self, self._main_controller.handler_key_1_0)
        self.sCt_pB_2_0 = QShortcut(u"5", self, self._main_controller.handler_key_2_0)
        self.sCt_pB_3_0 = QShortcut(u"8", self, self._main_controller.handler_key_3_0)
        self.sCt_pB_4_0 = QShortcut(u"/", self, self._main_controller.handler_key_4_0)
        self.sCt_pB_0_1 = QShortcut(u",", self, self._main_controller.handler_key_0_1)
        self.sCt_pB_1_1 = QShortcut(u"3", self, self._main_controller.handler_key_1_1)
        self.sCt_pB_2_1 = QShortcut(u"6", self, self._main_controller.handler_key_2_1)
        self.sCt_pB_3_1 = QShortcut(u"9", self, self._main_controller.handler_key_3_1)
        self.sCt_pB_4_1 = QShortcut(u"*", self, self._main_controller.handler_key_4_1)
        self.sCt_pB_all_time_0 = QShortcut(u"Enter", self, self._main_controller.handler_all_time_0)
        self.sCt_pB_all_time_1 = QShortcut(u"+", self, self._main_controller.handler_all_time_1)
        self.sCt_pB_all_time_2 = QShortcut(u"-", self, self._main_controller.handler_all_time_2)
        self.sCt_pB_all_time_3 = QShortcut(u"Backspace", self, self._main_controller.handler_all_time_3)

        self.sCt_pB_horns_menu.setAutoRepeat(False)
        self.sCt_pB_lights_menu.setAutoRepeat(False)
        self.sCt_pB_speaker_menu.setAutoRepeat(False)
        self.sCt_pB_settings_menu.setAutoRepeat(False)
        self.sCt_pB_1_0.setAutoRepeat(False)
        self.sCt_pB_2_0.setAutoRepeat(False)
        self.sCt_pB_3_0.setAutoRepeat(False)
        self.sCt_pB_4_0.setAutoRepeat(False)
        self.sCt_pB_0_1.setAutoRepeat(False)
        self.sCt_pB_1_1.setAutoRepeat(False)
        self.sCt_pB_2_1.setAutoRepeat(False)
        self.sCt_pB_3_1.setAutoRepeat(False)
        self.sCt_pB_4_1.setAutoRepeat(False)
        self.sCt_pB_all_time_0.setAutoRepeat(False)
        self.sCt_pB_all_time_1.setAutoRepeat(False)
        self.sCt_pB_all_time_2.setAutoRepeat(False)
        self.sCt_pB_all_time_3.setAutoRepeat(False)     
        
        """  # setup shortcuts
        self._ui.pB_key_1_0.setShortcut(u"2")
        self._ui.pB_key_2_0.setShortcut(u"5")
        self._ui.pB_key_3_0.setShortcut(u"8")
        self._ui.pB_key_4_0.setShortcut(u"/")
        self._ui.pB_key_0_1.setShortcut(u",")
        self._ui.pB_key_1_1.setShortcut(u"3")
        self._ui.pB_key_2_1.setShortcut(u"6")
        self._ui.pB_key_3_1.setShortcut(u"9")
        self._ui.pB_key_4_1.setShortcut(u"*")
        self._ui.pB_all_time_0.setShortcut(u"Enter")
        self._ui.pB_all_time_1.setShortcut(u"+")
        self._ui.pB_all_time_2.setShortcut(u"-")
        self._ui.pB_all_time_3.setShortcut(u"Backspace") """

        self._ui.pTE_console.setCenterOnScroll(True) 

                # mapping to handler functions
        self._ui.pB_key_1_0.clicked.connect(self._main_controller.handler_key_1_0)
        self._ui.pB_key_2_0.clicked.connect(self._main_controller.handler_key_2_0)
        self._ui.pB_key_3_0.clicked.connect(self._main_controller.handler_key_3_0)
        self._ui.pB_key_4_0.clicked.connect(self._main_controller.handler_key_4_0)
        self._ui.pB_key_0_1.clicked.connect(self._main_controller.handler_key_0_1)
        self._ui.pB_key_1_1.clicked.connect(self._main_controller.handler_key_1_1)
        self._ui.pB_key_2_1.clicked.connect(self._main_controller.handler_key_2_1)
        self._ui.pB_key_3_1.clicked.connect(self._main_controller.handler_key_3_1)
        self._ui.pB_key_4_1.clicked.connect(self._main_controller.handler_key_4_1)
        self._ui.pB_all_time_0.clicked.connect(self._main_controller.handler_all_time_0)
        self._ui.pB_all_time_1.clicked.connect(self._main_controller.handler_all_time_1)
        self._ui.pB_all_time_2.clicked.connect(self._main_controller.handler_all_time_2)
        self._ui.pB_all_time_3.clicked.connect(self._main_controller.handler_all_time_3)

        self._ui.pB_all_time_0.setText("THW Horn")
        self._ui.pB_all_time_1.setText("Train Horn")
        self._ui.pB_all_time_2.setText("Preset 6\n Horn Sound")
        self._ui.pB_all_time_3.setText("All Horns")

        self._model.lights_changed.connect(self.update_button_visualisation_lights)
        self._model.horns_changed.connect(self.update_button_visualisation_horns)
        self._model.horns_changed.connect(self.update_button_visualisation_allTimeAccess)
        self._main_controller.soundPlayer.SoundSelected.connect(self.update_button_visualisation_speaker)
        self._main_controller.settingsManager.NewSettings.connect(self.update_button_visualisation_settings)

        """ self._ui.pB_horns.pressed.connect(self._main_controller.set_horns_mode)
        self._ui.pB_lights.pressed.connect(self._main_controller.set_lights_mode)
        self._ui.pB_speaker.pressed.connect(self._main_controller.set_speaker_mode)
        self._ui.pB_settings.pressed.connect(self._main_controller.set_settings_mode)
 """
        # listen for model event signals
        # connect the method to update the ui to the slots of the model
        # if model sends/emits a signal the ui gets notified
        """ self._model.amount_changed.connect(self.on_amount_changed)
        self._model.even_odd_changed.connect(self.on_even_odd_changed)
        self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        self._model.users_changed.connect(self.on_list_changed)
        
        # set a default value
        self._main_controller.change_amount(42) """
        self._model.gui_mode_changed.connect(self.set_gui_mode)
        self._main_controller.soundPlayer.SoundSelected.connect(self.appendToConsole)

    @pyqtSlot()
    def test_shortcut(self):
        print("shortcut triggered")

    @pyqtSlot(int)
    def set_gui_mode(self, mode: int):
        if mode == self._model.HORNS_MODE:
            self.set_horn_page()
            self.update_button_visualisation_horns()
        elif mode == self._model.LIGHTS_MODE:
            self.set_lights_page()
            self.update_button_visualisation_lights()
        elif mode == self._model.SPEAKER_MODE:
            self.set_speaker_page()
            self.update_button_visualisation_speaker()
        elif mode == self._model.SETTINGS_MODE:
            self.set_util_page()
            self.update_button_visualisation_settings()

        self.update_button_visualisation_allTimeAccess()

    @pyqtSlot()
    def update_button_visualisation_lights(self):
        """
        self.lights_config = {"activate_lightbar_front": 0,
                              "activate_mode_lightbar_front": 0,
                              "activate_lightbar_back": 0,
                              "activate_mode_lightbar_back": 0,
                              "activate_flasher_grill": 0,
                              "activate_mode_flasher_grill": 0,
                              "activate_flasher_roof": 0,
                              "selection_flash_pattern_roof": 0,
                              "activate_worklight_roof": 0}
        """
        if self._model.get_gui_mode() == self._model.LIGHTS_MODE:
            config = self._model.get_lights_config()
            self._ui.pB_key_1_0.setStyleSheet(f"background-color: {self.activated_color if config['activate_lightbar_front'] else self.disactivated_color}")
            self._ui.pB_key_2_0.setStyleSheet(f"background-color: {self.activated_color if config['activate_mode_lightbar_front'] else self.disactivated_color}")
            self._ui.pB_key_3_0.setStyleSheet(f"background-color: {self.activated_color if config['activate_flasher_grill'] else self.disactivated_color}")
            self._ui.pB_key_4_0.setStyleSheet(f"background-color: {self.activated_color if config['activate_mode_flasher_grill'] else self.disactivated_color}")
            self._ui.pB_key_0_1.setStyleSheet(f"background-color: {self.activated_color if config['activate_lightbar_back'] else self.disactivated_color}")
            self._ui.pB_key_1_1.setStyleSheet(f"background-color: {self.activated_color if config['activate_mode_lightbar_back'] else self.disactivated_color}")
            self._ui.pB_key_2_1.setStyleSheet(f"background-color: {self.activated_color if config['activate_flasher_roof'] else self.disactivated_color}")
            self._ui.pB_key_3_1.setStyleSheet(f"background-color: {self.activated_color if config['selection_flash_pattern_roof'] else self.disactivated_color}")
            self._ui.pB_key_4_1.setStyleSheet(f"background-color: {self.activated_color if config['activate_worklight_roof'] else self.disactivated_color}")

    @pyqtSlot()
    def update_button_visualisation_horns(self):
        """
        self.horns_config = {"activate_thw_horn": 0,
                             "activate_train_horn": 0,
                             "activate_all_horns": 0,
                             "selection_horn_sound": 0,
                             "activate_horn_sound": 0}
        """
        if self._model.get_gui_mode() == self._model.HORNS_MODE:
            config = self._model.get_horns_config()
            
            self._ui.pB_key_1_0.setStyleSheet(f"background-color: {self.activated_color if config['selection_horn_sound'] == 0 else self.disactivated_color}")
            self._ui.pB_key_2_0.setStyleSheet(f"background-color: {self.activated_color if config['selection_horn_sound'] == 1 else self.disactivated_color}")
            self._ui.pB_key_3_0.setStyleSheet(f"background-color: {self.activated_color if config['selection_horn_sound'] == 2 else self.disactivated_color}")
            self._ui.pB_key_4_0.setStyleSheet(f"background-color: {self.activated_color if config['selection_horn_sound'] == 3 else self.disactivated_color}")
            self._ui.pB_key_0_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_1_1.setStyleSheet(f"background-color: {self.activated_color if config['activate_horn_sound'] else self.disactivated_color}")
            self._ui.pB_key_1_1.setText(f"play/stop\n Midi {config['selection_horn_sound']}")
            self._ui.pB_key_2_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_3_1.setStyleSheet(f"background-color: {self.activated_color if config['selection_horn_sound'] == 4 else self.disactivated_color}")
            self._ui.pB_key_4_1.setStyleSheet(f"background-color: {self.activated_color if config['selection_horn_sound'] == 5 else self.disactivated_color}")

    @pyqtSlot()
    def update_button_visualisation_speaker(self):
        if self._model.get_gui_mode() == self._model.SPEAKER_MODE:
            current_index = self._main_controller.soundPlayer.get_selection_index()
            self._ui.pB_key_1_0.setStyleSheet(f"background-color: {self.activated_color if current_index == 0 else self.disactivated_color}")
            self._ui.pB_key_2_0.setStyleSheet(f"background-color: {self.activated_color if current_index == 1 else self.disactivated_color}")
            self._ui.pB_key_3_0.setStyleSheet(f"background-color: {self.activated_color if current_index == 2 else self.disactivated_color}")
            self._ui.pB_key_4_0.setStyleSheet(f"background-color: {self.activated_color if current_index == 3 else self.disactivated_color}")
            self._ui.pB_key_0_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_1_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_1_1.setText(f"play/stop\n Sound {current_index}")
            self._ui.pB_key_2_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_3_1.setStyleSheet(f"background-color: {self.activated_color if current_index == 4 else self.disactivated_color}")
            self._ui.pB_key_4_1.setStyleSheet(f"background-color: {self.activated_color if current_index == 5 else self.disactivated_color}")

    @pyqtSlot()
    def update_button_visualisation_settings(self):
        if self._model.get_gui_mode() == self._model.SETTINGS_MODE:
            brightness = self._main_controller.settingsManager.get_current_brightness()
            self._ui.pB_key_1_0.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_2_0.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_3_0.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_3_0.setText(f"Aktuell Wert\n {brightness}")
            self._ui.pB_key_4_0.setStyleSheet(f"background-color: { self.disactivated_color}")
            self._ui.pB_key_0_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_1_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_2_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_3_1.setStyleSheet(f"background-color: {self.disactivated_color}")
            self._ui.pB_key_4_1.setStyleSheet(f"background-color: {self.disactivated_color}")

    @pyqtSlot()
    def update_button_visualisation_allTimeAccess(self):
        """
        self.horns_config = {"activate_thw_horn": 0,
                             "activate_train_horn": 0,
                             "activate_all_horns": 0,
                             "selection_horn_sound": 0,
                             "activate_horn_sound": 0}
        """
        config = self._model.get_horns_config()
        self._ui.pB_all_time_0.setStyleSheet(f"background-color: {self.activated_color if config['activate_thw_horn'] else self.disactivated_color}")
        self._ui.pB_all_time_1.setStyleSheet(f"background-color: {self.activated_color if config['activate_train_horn'] else self.disactivated_color}")
        self._ui.pB_all_time_2.setStyleSheet(f"background-color: {self.activated_color if config['selection_horn_sound'] == 6 else self.disactivated_color}")
        self._ui.pB_all_time_3.setStyleSheet(f"background-color: {self.activated_color if config['activate_all_horns'] else self.disactivated_color}")

    def set_horn_page(self):
        config = self._model.get_horns_config()
        self._ui.pTE_console.appendPlainText("Horn page loaded.")
        self._ui.pTE_console.ensureCursorVisible()
        self._ui.pB_key_1_0.setText("preset 0")
        self._ui.pB_key_2_0.setText("preset 1")
        self._ui.pB_key_3_0.setText("preset 2")
        self._ui.pB_key_4_0.setText("preset 3")
        self._ui.pB_key_0_1.setText("prev.\n Midi")
        self._ui.pB_key_1_1.setText(f"play/stop\n Midi {config['selection_horn_sound']}")
        self._ui.pB_key_2_1.setText("next\n Midi")
        self._ui.pB_key_3_1.setText("preset 4")
        self._ui.pB_key_4_1.setText("preset 5")

    def set_speaker_page(self):
        current_index = self._main_controller.soundPlayer.get_selection_index()

        self._ui.pTE_console.appendPlainText("Speaker page loaded.")
        self._ui.pTE_console.ensureCursorVisible()
        self._ui.pB_key_1_0.setText("preset 0")
        self._ui.pB_key_2_0.setText("preset 1")
        self._ui.pB_key_3_0.setText("preset 2")
        self._ui.pB_key_4_0.setText("preset 3")
        self._ui.pB_key_0_1.setText("prev.\n Sound")
        self._ui.pB_key_1_1.setText(f"play/stop\n Sound {current_index}")
        self._ui.pB_key_2_1.setText("next\n Sound")
        self._ui.pB_key_3_1.setText("preset 4")
        self._ui.pB_key_4_1.setText("preset 5")
         
    def set_util_page(self):
        brightness = self._main_controller.settingsManager.get_current_brightness()
        self._ui.pTE_console.appendPlainText("settings page loaded.")
        self._ui.pTE_console.ensureCursorVisible()
        self._ui.pB_key_1_0.setText("Bildschirm\n heller")
        self._ui.pB_key_2_0.setText("Bildschirm\n dunkler")
        self._ui.pB_key_3_0.setText(f"Aktuell Wert\n {brightness}")
        self._ui.pB_key_4_0.setText("unused")
        self._ui.pB_key_0_1.setText("unused")
        self._ui.pB_key_1_1.setText("unused")
        self._ui.pB_key_2_1.setText("unused")
        self._ui.pB_key_3_1.setText("unused")
        self._ui.pB_key_4_1.setText("unused")

    def set_lights_page(self):
        self._ui.pTE_console.appendPlainText("Lights page loaded.")
        self._ui.pTE_console.ensureCursorVisible()
        self._ui.pB_key_1_0.setText("LT Vorne\n aktivieren")
        self._ui.pB_key_2_0.setText("LT Vorne\n Modus")
        self._ui.pB_key_3_0.setText("L-KhlGrl\n aktivieren")
        self._ui.pB_key_4_0.setText("L-KhlGrl\n Modus")
        self._ui.pB_key_0_1.setText("LT Hinten\n aktivieren")
        self._ui.pB_key_1_1.setText("LT Hinten\n Modus")
        self._ui.pB_key_2_1.setText("FL Dach\n aktivieren")
        self._ui.pB_key_3_1.setText("FL Dach\n Modus")
        self._ui.pB_key_4_1.setText("Arb.\n Sch.-W")

    @pyqtSlot(str)
    def appendToConsole(self, str_val):
        self._ui.pTE_console.appendPlainText(str_val)

    
"""     @pyqtSlot(str)
    def on_even_odd_changed(self, value):
        self._ui.label_even_odd.setText(value)

    @pyqtSlot(bool)
    def on_enable_reset_changed(self, value):
        self._ui.pushButton_reset.setEnabled(value)

    @pyqtSlot(list)
    def on_list_changed(self, value):
        self._ui.listWidget_names.clear()
        self._ui.listWidget_names.addItems(value) """