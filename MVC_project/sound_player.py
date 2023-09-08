import os
from PyQt5.QtCore import *
import pygame
import wave

class Player(QObject):
    base_path =  "/home/carbage/carbage_run_audi/MVC_project/sound_files/instant_buttons"

    # soundFiles = ["sound_file_0_corrected.wav", "sound_file_1_corrected.wav", "sound_file_2_corrected.wav",
    #                "sound_file_3_corrected.wav", "sound_file_4_corrected.wav", "sound_file_5_corrected.wav"]
    
    presetLookUpTable = [0, 1, 2, 3, 4, 5]  # TODO unused removes
    SoundSelected = pyqtSignal(str)
    SoundStarted = pyqtSignal()
    SoundStopped = pyqtSignal()
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        if os.name == 'nt':
            self.base_path = r'C:\Users\rich_\OneDrive\raspberry_carbage\MVC_project\sound_files\instant_buttons'

        pygame.mixer.init()

        self.selectionIndex = 0        
        self.resolvedSoundFiles = []

        preset_selection = ["siren.mp3", "siren-brr-brr", "wail", "yelp", "106-miles", "musica-elevador-short"]

        # 'search for the preset files'
        for preset_file_name in preset_selection:
            found = False
            for root, dirs, files in os.walk(self.base_path, topdown=False):
                for name in files:
                    if preset_file_name in name:
                        self.resolvedSoundFiles.append(os.path.join(root, name))
                        found = True
            assert found

        # append the reset
        for root, dirs, files in os.walk(self.base_path, topdown=False):
            for name in files:
                if not (os.path.join(root, name) in self.resolvedSoundFiles):
                    self.resolvedSoundFiles.append(os.path.join(root, name))

        self.currentSoundFile = self.resolvedSoundFiles[self.selectionIndex]
        print(self.currentSoundFile)
        assert os.path.exists(self.currentSoundFile)

        self.loadSoundFile()
    
    def loadSoundFile(self):
        
        self.currentSoundFile = self.resolvedSoundFiles[self.selectionIndex]
        pygame.mixer.music.load(self.currentSoundFile)

    @pyqtSlot()
    def start_sound(self):
        # print(f"entry start_sound:{process.memory_info().rss}")  # in bytes
        if pygame.mixer.music.get_busy():
            self.stop_sound()

        self.loadSoundFile()
        # print(f"after load :{process.memory_info().rss}")  # in bytes
        pygame.mixer.music.play()
        self.SoundStarted.emit()
        
    @pyqtSlot()
    def stop_sound(self):
        # print(f"entry stop_sound:{process.memory_info().rss}")  # in bytes
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
 
        self.SoundStopped.emit()
        # print(f"return stop_sound:{process.memory_info().rss}")  # in bytes

    @pyqtSlot()
    def next_sound(self):
        if (self.selectionIndex + 1) == len(self.resolvedSoundFiles):
            self.selectionIndex = 0
        else:
            self.selectionIndex = self.selectionIndex + 1 
        self.currentSoundFile = self.resolvedSoundFiles[self.selectionIndex]
        self.SoundSelected.emit("next: " + self.currentSoundFile)

    @pyqtSlot()
    def prev_sound(self):
        if (self.selectionIndex - 1) < 0:
            self.selectionIndex = len(self.resolvedSoundFiles) - 1
        else:
            self.selectionIndex = self.selectionIndex - 1 
        self.currentSoundFile = self.resolvedSoundFiles[self.selectionIndex]
        self.SoundSelected.emit("prev: " + self.currentSoundFile)

    def _playPreset(self, index):
        self.selectionIndex = self.presetLookUpTable[index]
        self.currentSoundFile = self.resolvedSoundFiles[self.selectionIndex]
        self.SoundSelected.emit("play: " + self.currentSoundFile)
        
        self.start_sound()

    @pyqtSlot()
    def playPreset0(self):
        self._playPreset(0)

    @pyqtSlot()
    def playPreset1(self):
        self._playPreset(1)
    
    @pyqtSlot()
    def playPreset2(self):
        self._playPreset(2)
    
    @pyqtSlot()
    def playPreset3(self):
        self._playPreset(3)

    @pyqtSlot()
    def playPreset4(self):
        self._playPreset(4)

    @pyqtSlot()
    def playPreset5(self):
        self._playPreset(5)

    def get_selection_index(self):
        return self.selectionIndex
    
    def get_file_name(self, index=None):
        if index is None:
            filename = self.currentSoundFile
        else:
            mainIndex = self.presetLookUpTable[index]
            filename = self.resolvedSoundFiles[mainIndex]
        
        return filename.replace(self.base_path, "").replace(".mp3", "").replace("/", "")[:10]
            

if __name__ == "__main__":

    from PyQt5.QtWidgets import *
    import os, psutil
    process = psutil.Process()
     

    # Only needed for access to command line arguments
    import sys

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)

    player = Player()

    widget = QWidget()
    layout = QVBoxLayout()
    pB_0 = QPushButton(player.get_file_name(0))
    pB_0.clicked.connect(player.playPreset0)
    pB_1 = QPushButton(player.get_file_name(1))
    pB_1.clicked.connect(player.playPreset1)
    pB_2 = QPushButton(player.get_file_name(2))
    pB_2.clicked.connect(player.playPreset2)
    pB_3 = QPushButton(player.get_file_name(3))
    pB_3.clicked.connect(player.playPreset3)
    pB_4 = QPushButton(player.get_file_name(4))
    pB_4.clicked.connect(player.playPreset4)
    pB_5 = QPushButton(player.get_file_name(5))
    pB_5.clicked.connect(player.playPreset5)
    pB_prev = QPushButton("prev")
    pB_prev.clicked.connect(player.prev_sound)
    pB_play = QPushButton("play: " + player.get_file_name())
    pB_play.clicked.connect(player.start_sound)
    pB_next = QPushButton("next")
    pB_next.clicked.connect(player.next_sound)

    layout.addWidget(pB_0)
    layout.addWidget(pB_1)
    layout.addWidget(pB_2)
    layout.addWidget(pB_3)
    layout.addWidget(pB_4)
    layout.addWidget(pB_5)
    layout.addWidget(pB_prev)
    layout.addWidget(pB_play)
    layout.addWidget(pB_next)

    widget.setLayout(layout)
    widget.show()
    # Create a Qt widget, which will be our window.
    
    # Start the event loop.
    app.exec()


    # Your application won't reach here until you exit and the event
    # loop has stopped.
