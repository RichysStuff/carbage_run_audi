from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtCore import pyqtSlot

class Model(QObject):
    HORNS_MODE = 0
    LIGHTS_MODE = 1
    SPEAKER_MODE = 2
    SETTINGS_MODE = 3

    horns_changed = pyqtSignal()
    lights_changed = pyqtSignal()
    brightness_changed = pyqtSignal()
    gui_mode_changed = pyqtSignal(int)  

    nHornsSounds = 10
    nFlashPatternsRoof = 3

    """
    horn sound ID   comment
    0               TBD
    1               TBD
    2               TBD
    3               TBD
    4               TBD
    5               TBD
    6               alternating THW horn
    """

    def set_lights_config(self, config: dict):
        self.lights_config = config
        self.lights_changed.emit()
        print(config)

    def get_lights_config(self):
        return self.lights_config
    
    def set_horns_config(self, config: dict):
        self.horns_config = config
        self.horns_changed.emit()
        print(config)

    def get_horns_config(self):
        return self.horns_config
    
    def set_brightness(self, val: int):
        self._brightness = val
        self.brightness_changed.emit(self._brightness)

    def get_brightness(self):
        return self._brightness
    
    def set_gui_mode(self, val: int):
        self._gui_mode = val
        self.gui_mode_changed.emit(self._gui_mode)

    def get_gui_mode(self):
        return self._gui_mode
    
    def encode_horns(self):
        """ 
        self.horns_config = {"activate_thw_horn": 0,    1 bit    7	
                             "activate_train_horn": 0,  1 bit    6
                             "activate_all_horns": 0,   1 bit    5
                             "selection_horn_sound": 0, 4 bit    1
                             "activate_horn_sound": 0}  1 bit    0  offset
                             """
        
        out = self.horns_config["activate_thw_horn"] << 7
        out = out | (self.horns_config["activate_train_horn"] << 6)
        out = out | (self.horns_config["activate_all_horns"] << 5)
        out = out | (self.horns_config["selection_horn_sound"] << 1) 
        return out | self.horns_config["activate_horn_sound"]
    
    def encode_lights(self):
        """ 
        self.lights_config = {"activate_lightbar_front": 0,         1 bit   11
                              "activate_mode_lightbar_front": 0,    1 bit   10	
                              "activate_lightbar_back": 0,          1 bit   9
                              "activate_mode_lightbar_back": 0,     1 bit   8
                              "activate_flasher_grill": 0,          1 bit   7
                              "activate_mode_flasher_grill": 0,     1 bit   6
                              "activate_flasher_roof": 0,           1 bit   5
                              "selection_flash_pattern_roof": 0,    4 bit   1
                              "activate_worklight_roof": 0}         1 bit   0
                             """
        
        out = self.lights_config["activate_lightbar_front"] << 11
        out = out | (self.lights_config["activate_mode_lightbar_front"] << 10)
        out = out | (self.lights_config["activate_lightbar_back"] << 9)
        out = out | (self.lights_config["activate_mode_lightbar_back"] << 8)
        out = out | (self.lights_config["activate_flasher_grill"] << 7)
        out = out | (self.lights_config["activate_mode_flasher_grill"] << 6)
        out = out | (self.lights_config["activate_flasher_roof"] << 5)
        out = out | (self.lights_config["selection_flash_pattern_roof"] << 1)
        return out | self.lights_config["activate_worklight_roof"]
    
    @pyqtSlot()
    def reset_mode_parameters(self):
        
        if self.reset_mode_vals_nxtCyl:
            self.reset_mode_vals_nxtCyl = False
            config = self.lights_config
            config["activate_mode_lightbar_front"] = 0
            config["activate_mode_lightbar_back"] = 0
            config["activate_mode_flasher_grill"] = 0
            print("reseted mode values")
            self.set_lights_config(config)
        
        elif self.lights_config["activate_mode_lightbar_front"] != 0 or \
            self.lights_config["activate_mode_lightbar_back"] != 0 or \
            self.lights_config["activate_mode_flasher_grill"] != 0:
            print("reset mode values detection triggered")
            self.reset_mode_vals_nxtCyl = True


    @pyqtSlot()
    def start_timer(self):
        self.mode_val_reset_timer.start(500)

    @pyqtSlot()
    def stop_timer(self):
        self.mode_val_reset_timer.stop(0)
        
    def __init__(self):
        super().__init__()

        self.horns_config = {"activate_thw_horn": 0,
                             "activate_train_horn": 0,
                             "activate_all_horns": 0,
                             "selection_horn_sound": 0,
                             "activate_horn_sound": 0}
        
        self.lights_config = {"activate_lightbar_front": 0,
                              "activate_mode_lightbar_front": 0,
                              "activate_lightbar_back": 0,
                              "activate_mode_lightbar_back": 0,
                              "activate_flasher_grill": 0,
                              "activate_mode_flasher_grill": 0,
                              "activate_flasher_roof": 0,
                              "selection_flash_pattern_roof": 0,
                              "activate_worklight_roof": 0}

        self._brightness = 127

        self._gui_mode = self.HORNS_MODE
        self.reset_mode_vals_nxtCyl = False
        self.mode_val_reset_timer = QTimer(self)
        self.mode_val_reset_timer.timeout.connect(self.reset_mode_parameters)
