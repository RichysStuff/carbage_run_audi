from PyQt5.QtCore import *

class Manager(QObject):
    NewSettings = pyqtSignal()
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.brightness = 100
        self.minBrightness = 40
        self.maxBrightness = 254
    
    @pyqtSlot()
    def _write_new_brightness(self):
        with open('/sys/class/backlight/10-0045/brightness', 'w') as f:
            f.write(f"{self.brightness}")
        self.NewSettings.emit()

    @pyqtSlot()
    def increaseBrightness(self):
        print("increase")
        if (self.brightness + 10)<=self.maxBrightness:
            self.brightness = self.brightness + 10
        else:
            self.brightness = self.maxBrightness
        self._write_new_brightness()
        

    @pyqtSlot()
    def decreaseBrightness(self):
        print("decrease")
        if (self.brightness - 10) >= self.minBrightness:
            self.brightness = self.brightness - 10
        else:
            self.brightness = self.minBrightness
        self._write_new_brightness()

    def get_current_brightness(self):
        return self.brightness


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

    manager = Manager()

    widget = QWidget()
    layout = QVBoxLayout()
    pB_0 = QPushButton("increase")
    pB_0.clicked.connect(manager.increaseBrightness)
    pB_1 = QPushButton("decrease")
    pB_1.clicked.connect(manager.decreaseBrightness)
    

    layout.addWidget(pB_0)
    layout.addWidget(pB_1)
  
    widget.setLayout(layout)
    widget.show()
    # Create a Qt widget, which will be our window.
    
    # Start the event loop.
    app.exec()


    # Your application won't reach here until you exit and the event
    # loop has stopped.
