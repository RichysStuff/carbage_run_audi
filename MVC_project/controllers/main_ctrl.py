from PyQt5.QtCore import QObject, pyqtSlot, QTimer
from sound_player import Player as Player_Sound
from settings_manager import Manager as Manager_Settings
from MQTT_handler import MqttHandler as Handler_MQTT

class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        
        self._model = model
        self._model.lights_changed.connect(self.update_remote_light_config)
        self._model.horns_changed.connect(self.update_remote_horn_config)
        
        self.soundPlayer = Player_Sound()
        self.settingsManager = Manager_Settings()
        self.mqttHandler = Handler_MQTT()
        self.mqttHandler.connectedSignal.connect(self._model.start_timer)
        self.mqttHandler.disconnectedSignal.connect(self._model.stop_timer)
        self.mqttHandler.connect_to_broker()

        self._timer = QTimer(parent=self)
        self._timer.setInterval(2000)
        self._timer.timeout.connect(self.update_remote_light_config)
        self._timer.timeout.connect(self.update_remote_horn_config)
        self.mqttHandler.connectedSignal.connect(self._timer.start)
        self.mqttHandler.disconnectedSignal.connect(self._timer.stop)

    @pyqtSlot()
    def set_horns_mode(self):
        self._model.set_gui_mode(self._model.HORNS_MODE)
    
    @pyqtSlot()
    def set_lights_mode(self):
        self._model.set_gui_mode(self._model.LIGHTS_MODE)
    
    @pyqtSlot()
    def set_speaker_mode(self):
        self._model.set_gui_mode(self._model.SPEAKER_MODE)
    
    @pyqtSlot()
    def set_settings_mode(self):
        self._model.set_gui_mode(self._model.SETTINGS_MODE)

    @pyqtSlot()
    def update_remote_horn_config(self):
        self.mqttHandler.pub_horn_config(self._model.encode_horns())

    @pyqtSlot()
    def update_remote_light_config(self):
        self.mqttHandler.pub_light_config(self._model.encode_lights())

    @pyqtSlot()
    def handler_key_1_0(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.toggle_horns_config_param("selection_horn_sound", 0)
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.playPreset0()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_lightbar_front")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            self.settingsManager.increaseBrightness()

    @pyqtSlot()
    def handler_key_2_0(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.toggle_horns_config_param("selection_horn_sound", 1)
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.playPreset1()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_mode_lightbar_front")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            self.settingsManager.decreaseBrightness()
    
    @pyqtSlot()
    def handler_key_3_0(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.toggle_horns_config_param("selection_horn_sound", 2)
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.playPreset2()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_flasher_grill")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            pass

    @pyqtSlot()
    def handler_key_4_0(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.toggle_horns_config_param("selection_horn_sound", 3)
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.playPreset3()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_mode_flasher_grill")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            pass

    @pyqtSlot()
    def handler_key_0_1(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.previous_horn_sound()
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.prev_sound()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_lightbar_back")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            pass

    @pyqtSlot()
    def handler_key_1_1(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.toggle_horns_config_param("activate_horn_sound")
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.start_sound()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_mode_lightbar_back")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            pass

    @pyqtSlot()
    def handler_key_2_1(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.next_horn_sound()
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.next_sound()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_flasher_roof")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            pass

    @pyqtSlot()
    def handler_key_3_1(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.toggle_horns_config_param("selection_horn_sound", 4)
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.playPreset4()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.next_flash_pattern_roof()
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            pass
    
    @pyqtSlot()
    def handler_key_4_1(self):
        if self._model._gui_mode == self._model.HORNS_MODE:
            self.toggle_horns_config_param("selection_horn_sound", 5)
        elif self._model._gui_mode == self._model.SPEAKER_MODE:
            self.soundPlayer.playPreset5()
        elif self._model._gui_mode == self._model.LIGHTS_MODE:
            self.toggle_lights_config_param("activate_worklight_roof")
        elif self._model._gui_mode == self._model.SETTINGS_MODE:
            pass

    @pyqtSlot()
    def handler_all_time_0(self):
        print("handler all time 0")
        self.toggle_horns_config_param("activate_thw_horn")


    @pyqtSlot()
    def handler_all_time_1(self):
        print("handler all time 1")
        self.toggle_horns_config_param("activate_train_horn")


    @pyqtSlot()
    def handler_all_time_2(self):
        print("handler all time 2")
        self.toggle_horns_config_param("selection_horn_sound", 6) 

    @pyqtSlot()
    def handler_all_time_3(self):
        print("handler all time 3")
        self.toggle_horns_config_param("activate_all_horns")

    def toggle_lights_config_param(self, param):
        config = self._model.get_lights_config()
        config[param] = not config[param]
        self._model.set_lights_config(config)

    def toggle_horns_config_param(self, param, value=None):
        config = self._model.get_horns_config()
        if value is not None:
            config[param] = value
        else:
            config[param] = not config[param]
        self._model.set_horns_config(config)

    def next_horn_sound(self):
        config = self._model.get_horns_config()
        if config["selection_horn_sound"] + 1 >= self._model.nHornsSounds:
            config["selection_horn_sound"] = 0
        else:
            config["selection_horn_sound"] = config["selection_horn_sound"] + 1
        
        self._model.set_horns_config(config)

    def previous_horn_sound(self):
        config = self._model.get_horns_config()
        if config["selection_horn_sound"] - 1 < 0:
            config["selection_horn_sound"] = self._model.nHornsSounds - 1
        else:
            config["selection_horn_sound"] = config["selection_horn_sound"] - 1
        
        self._model.set_horns_config(config)

    def next_flash_pattern_roof(self):
        config = self._model.get_lights_config()
        if config["selection_flash_pattern_roof"] + 1 >= self._model.nFlashPatternsRoof:
            config["selection_flash_pattern_roof"] = 0
        else:
            config["selection_flash_pattern_roof"] = config["selection_flash_pattern_roof"] + 1
        self._model.set_lights_config(config)