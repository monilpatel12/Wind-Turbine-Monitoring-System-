import sys
import random
import json
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QProgressBar, QDialogButtonBox


# Helper functions and class definitions for EnergyProduction, BladePitch, BatteryHealth, etc.
# (Include your EnergyProduction, BladePitch, BatteryHealth, GearboxHealth, WindSpeed, VibrationAnalysis classes here)

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 620)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 550, 151, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 471, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.statusLabel = QtWidgets.QLabel("Initial Text")  # You can set initial text or leave it empty
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)  # Align the text to center
        self.verticalLayout.addWidget(self.statusLabel)  # Add the label to the vertical layout

        self.animationLabel = QtWidgets.QLabel(Dialog)
        self.animationLabel.setGeometry(QtCore.QRect(20, 10, 471, 121))  # Adjust the geometry as needed
        self.initialAnimation = QtGui.QMovie("C:/Users/patel/OneDrive - Conestoga College/Desktop/Project/windmill.png")
        self.animationLabel.setMovie(self.initialAnimation)
        self.initialAnimation.start()


        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 150, 471, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 480, 469, 24))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 520, 151, 31))
        self.pushButton.setObjectName("pushButton")


        # Create a QFont object with the desired font size
        larger_font = QtGui.QFont()
        larger_font.setBold(True)
        larger_font.setPointSize(12)  # Set the font size, e.g., 12 points

        # Apply the larger font to specific labels
        self.label_9.setFont(larger_font)
        self.label_10.setFont(larger_font)
        self.label_11.setFont(larger_font)
        self.label_12.setFont(larger_font)
        self.label_13.setFont(larger_font)
        self.label_14.setFont(larger_font)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) 
        self.buttonBox.rejected.connect(Dialog.reject) 
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "Blade Pitch"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "Energy Production"))
        self.label_11.setText(_translate("Dialog", "Gearbox Health"))
        self.label_14.setText(_translate("Dialog", "Vibration Level"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label_13.setText(_translate("Dialog", "Wind Speed"))
        self.label_12.setText(_translate("Dialog", "Battery Health"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "TeextLabel"))
        self.pushButton.setText(_translate("Dialog", "Check Status"))

def read_json_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return None

def write_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

class EnergyProduction:
    def __init__(self):
        self.energy_production = 0
        self.file_name = 'energy_production.json'

    def read_data(self):
        try:
            with open(self.file_name, 'r') as file:
                self.energy_production = json.load(file)
        except FileNotFoundError:
            self.write_data()

    def write_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.energy_production, file)

    def update(self):
        self.read_data()
        self.energy_production += random.uniform(20, 60)
        self.energy_production = round(self.energy_production, 2)
        self.write_data()
        return self.energy_production
    
class BladePitch:
    def __init__(self):
        self.blade_pitch = 0
        self.file_name = 'blade_pitch.json'
        self.read_data()

    def read_data(self):
        data = read_json_file(self.file_name)
        if data is not None:
            self.blade_pitch = data

    def write_data(self):
        write_json_file(self.file_name, self.blade_pitch)

    def update(self):
        wind_speed = random.uniform(2, 15)
        self.blade_pitch = 30 if wind_speed < 5 else 15 if wind_speed < 10 else 0
        self.write_data()
        return self.blade_pitch

class BatteryHealth:
    def __init__(self):
        self.battery_health = 100
        self.file_name = 'battery_health.json'
        self.read_data()

    def read_data(self):
        data = read_json_file(self.file_name)
        if data is not None:
            self.battery_health = data

    def write_data(self):
        write_json_file(self.file_name, self.battery_health)

    def update(self):
        charge_rate = random.uniform(-5, 10)
        self.battery_health = max(min(self.battery_health + charge_rate, 100), 0)
        self.write_data()
        return self.battery_health

class GearboxHealth:
    def __init__(self):
        self.gearbox_health = 100
        self.file_name = 'gearbox_health.json'
        self.read_data()

    def read_data(self):
        data = read_json_file(self.file_name)
        if data is not None:
            self.gearbox_health = data

    def write_data(self):
        write_json_file(self.file_name, self.gearbox_health)

    def update(self):
        damage_rate = random.uniform(-5, 10)
        self.gearbox_health = max(min(self.gearbox_health + damage_rate, 100), 0)
        self.write_data()
        return self.gearbox_health

class WindSpeed:
    def __init__(self):
        self.wind_speed = 0
        self.file_name = 'wind_speed.json'
        self.read_data()

    def read_data(self):
        data = read_json_file(self.file_name)
        if data is not None:
            self.wind_speed = data

    def write_data(self):
        write_json_file(self.file_name, self.wind_speed)

    def update(self):
        self.wind_speed = round(random.uniform(2, 30), 2)
        self.write_data()
        return self.wind_speed

class VibrationAnalysis:
    def __init__(self):
        self.vibration_level = 0
        self.file_name = 'vibration_level.json'
        self.read_data()

    def read_data(self):
        data = read_json_file(self.file_name)
        if data is not None:
            self.vibration_level = data

    def write_data(self):
        write_json_file(self.file_name, self.vibration_level)

    def update(self):
        self.vibration_level = round(random.uniform(0, 10), 2)
        self.write_data()
        return self.vibration_level
    
class WindTurbineManagementSystem(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(WindTurbineManagementSystem, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.reset_data)

        # Initialize your logic classes
        self.energy = EnergyProduction()
        self.blade = BladePitch()
        self.battery = BatteryHealth()
        self.gearbox = GearboxHealth()
        self.wind = WindSpeed()
        self.vibration = VibrationAnalysis()
        

        # Define the units for each measurement
        units = {
        "energy_production": "kWh", 
        "blade_pitch": "degrees",
        "battery_health": "%",
        "gearbox_health": "%",
        "wind_speed": "m/s",
        "vibration_level": "mm/s"  
        }

        
        # Set up labels for displaying data (map these to the labels in your UI)
        self.label.setText(f'{self.energy.energy_production}')
        self.label_2.setText(f'{self.blade.blade_pitch}')
        self.label_3.setText(f'{self.battery.battery_health}')
        self.label_4.setText(f'{self.gearbox.gearbox_health}')
        self.label_5.setText(f'{self.wind.wind_speed}')
        self.label_6.setText(f'{self.vibration.vibration_level}')

        # Set initial label values to zero
        self.label.setText(f'0.00 {units["energy_production"]}')
        self.label_2.setText(f'0.00 {units["blade_pitch"]}')
        self.label_3.setText(f'0.00 {units["battery_health"]}')
        self.label_4.setText(f'0.00 {units["gearbox_health"]}')
        self.label_5.setText(f'0.00 {units["wind_speed"]}')
        self.label_6.setText(f'0.00 {units["vibration_level"]}')




        # Initialize the QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress_bar)
        self.progress_value = 0

        # Initialize progress bar to 0%
        self.progressBar.setValue(0)

        # Connect the Check Status button
        self.pushButton.clicked.connect(self.start_progress)

        # Connect the pushButton to update_data method
        self.pushButton.clicked.connect(self.update_data)

    def start_progress(self):
        self.progress_value = 0
        self.progressBar.setValue(0)
        self.timer.start(50)  # Update every 100 milliseconds

        # Change to fetching animation
        self.fetchingAnimation = QtGui.QMovie("C:/Users/patel/OneDrive - Conestoga College/Desktop/Project/wind-mill.gif")
        self.animationLabel.setMovie(self.fetchingAnimation)
        self.fetchingAnimation.start()

        # Start a delay timer for updating data
        self.delay_timer = QTimer(self)
        self.delay_timer.singleShot(3200, self.delayed_update_data)  # 5000 milliseconds = 5 seconds delay

    def delayed_update_data(self):
        # Stop the fetching animation
        self.fetchingAnimation.stop()

        # Update data and labels
        self.update_data()

        # Change to second GIF that keeps playing
        self.continuousAnimation = QtGui.QMovie("C:/Users/patel/OneDrive - Conestoga College/Desktop/Project/completed.gif")
        self.animationLabel.setMovie(self.continuousAnimation)
        self.continuousAnimation.start()


    def update_progress_bar(self):
        self.progress_value += 2
        self.progressBar.setValue(self.progress_value)
        if self.progress_value >= 100:
            self.timer.stop()
            self.load_data()

    def load_data(self):
        # Load or update data here after progress bar completes
        
        self.update_data()
    
    def reset_data(self):
        # Reset data values to zero and update labels
        self.energy.energy_production = 0
        self.blade.blade_pitch = 0
        self.battery.battery_health = 0
        self.gearbox.gearbox_health = 0
        self.wind.wind_speed = 0
        self.vibration.vibration_level = 0

        # Update the labels with reset values
        self.label.setText('0')
        self.label_2.setText('0')
        self.label_3.setText('0')
        self.label_4.setText('0')
        self.label_5.setText('0')
        self.label_6.setText('0')
        


    def update_data(self):
        # Update each component and refresh the labels
        energy_production = self.energy.update()
        blade_pitch = self.blade.update()
        battery_health = self.battery.update()
        gearbox_health = self.gearbox.update()
        wind_speed = self.wind.update()
        vibration_level = self.vibration.update()

        # Define the units for each measurement
        units = {
        "energy_production": "kWh",  
        "blade_pitch": "degrees",
        "battery_health": "%",
        "gearbox_health": "%",
        "wind_speed": "m/s",
        "vibration_level": "mm/s"  
        }

        

        # Update the labels with the new data and units
        self.label.setText(f'{energy_production:.2f} {units["energy_production"]}')
        self.label_2.setText(f'{blade_pitch:.2f} {units["blade_pitch"]}')
        self.label_3.setText(f'{battery_health:.2f} {units["battery_health"]}')
        self.label_4.setText(f'{gearbox_health:.2f} {units["gearbox_health"]}')
        self.label_5.setText(f'{wind_speed:.2f} {units["wind_speed"]}')
        self.label_6.setText(f'{vibration_level:.2f} {units["vibration_level"]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = WindTurbineManagementSystem()
    mainWin.show()
    sys.exit(app.exec_())
