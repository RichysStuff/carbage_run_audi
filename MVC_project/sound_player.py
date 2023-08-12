import os
from PyQt5.QtCore import *
import pyaudio
import wave

class Player(QObject):
    base_path =  "/home/carbage/carbage_run_audi/MVC_project/sound_files"
    soundFiles = ["sound_file_0_corrected.wav", "sound_file_1_corrected.wav", "sound_file_2_corrected.wav",
                  "sound_file_3_corrected.wav", "sound_file_4_corrected.wav", "sound_file_5_corrected.wav"]
    presetLookUpTable = [0, 1, 2, 3, 4, 5]  # index --> index resolved names
    SoundSelected = pyqtSignal(str)
    SoundStarted = pyqtSignal()
    SoundStopped = pyqtSignal()
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        self.stream = None
        self.wf = None
        self.selectionIndex = 0

        if os.name == 'nt':
            self.base_path = r'C:\Users\rich_\OneDrive\raspberry_carbage\MVC_project\sound_files'

        self.resolvedSoundFiles = [os.path.join(self.base_path, sound_file) for sound_file in self.soundFiles]
        self.currentSoundFile = self.resolvedSoundFiles[self.selectionIndex]
        print(self.currentSoundFile)
        assert os.path.exists(self.currentSoundFile)

        self.loadSoundFile()

        # define callback
    def _callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
    
    def loadSoundFile(self):
        # you audio here
        self.currentSoundFile = self.resolvedSoundFiles[self.selectionIndex]
        self.wf = wave.open(self.currentSoundFile, 'rb')

        # instantiate PyAudio
        self.p = pyaudio.PyAudio()

        # open stream using callback
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                    channels=self.wf.getnchannels(),
                                    rate=self.wf.getframerate(),
                                    output=True, start=False,
                                    frames_per_buffer=8000,
                                    stream_callback=self._callback)

    @pyqtSlot()
    def start_sound(self):
        # print(f"entry start_sound:{process.memory_info().rss}")  # in bytes
        self.stop_sound()

        self.loadSoundFile()
        # print(f"after load :{process.memory_info().rss}")  # in bytes
        self.stream.start_stream()
        self.SoundStarted.emit()
        
    @pyqtSlot()
    def stop_sound(self):
        # print(f"entry stop_sound:{process.memory_info().rss}")  # in bytes
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()
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
    pB_0 = QPushButton("preset 0")
    pB_0.clicked.connect(player.playPreset0)
    pB_1 = QPushButton("preset 1")
    pB_1.clicked.connect(player.playPreset1)
    pB_2 = QPushButton("preset 2")
    pB_2.clicked.connect(player.playPreset2)
    pB_3 = QPushButton("preset 3")
    pB_3.clicked.connect(player.playPreset3)
    pB_4 = QPushButton("preset 4")
    pB_4.clicked.connect(player.playPreset4)
    pB_5 = QPushButton("preset 5")
    pB_5.clicked.connect(player.playPreset5)
    pB_prev = QPushButton("prev")
    pB_prev.clicked.connect(player.prev_sound)
    pB_play = QPushButton("play")
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
