import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QWidget, QLabel, QFormLayout
import numpy as np

class CalcApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 400, 400)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        self.form_layout = QFormLayout()

        # Inputs for Speed
        self.distance_input = QLineEdit()
        self.time_input = QLineEdit()
        self.speed_result = QLabel("Speed: ")

        # Inputs for Acceleration
        self.initial_speed_input = QLineEdit()
        self.final_speed_input = QLineEdit()
        self.accel_time_input = QLineEdit()
        self.acceleration_result = QLabel("Acceleration: ")

        # Inputs for Density
        self.mass_input = QLineEdit()
        self.volume_input = QLineEdit()
        self.density_result = QLabel("Density: ")

        # Inputs for Power
        self.force_input = QLineEdit()
        self.power_speed_input = QLineEdit()
        self.power_result = QLabel("Power: ")

        # Adding Speed inputs to form layout
        self.form_layout.addRow("Distance (m):", self.distance_input)
        self.form_layout.addRow("Time (s):", self.time_input)
        self.form_layout.addRow(self.speed_result)

        # Adding Acceleration inputs to form layout
        self.form_layout.addRow("Initial Speed (m/s):", self.initial_speed_input)
        self.form_layout.addRow("Final Speed (m/s):", self.final_speed_input)
        self.form_layout.addRow("Time (s):", self.accel_time_input)
        self.form_layout.addRow(self.acceleration_result)

        # Adding Density inputs to form layout
        self.form_layout.addRow("Mass (kg):", self.mass_input)
        self.form_layout.addRow("Volume (m³):", self.volume_input)
        self.form_layout.addRow(self.density_result)

        # Adding Power inputs to form layout
        self.form_layout.addRow("Force (N):", self.force_input)
        self.form_layout.addRow("Speed (m/s):", self.power_speed_input)
        self.form_layout.addRow(self.power_result)

        layout.addLayout(self.form_layout)

        self.speed_button = QPushButton("Calculate Speed")
        self.speed_button.clicked.connect(self.speed)
        layout.addWidget(self.speed_button)

        self.acceleration_button = QPushButton("Calculate Acceleration")
        self.acceleration_button.clicked.connect(self.acceleration)
        layout.addWidget(self.acceleration_button)

        self.density_button = QPushButton("Calculate Density")
        self.density_button.clicked.connect(self.density)
        layout.addWidget(self.density_button)

        self.power_button = QPushButton("Calculate Power")
        self.power_button.clicked.connect(self.power)
        layout.addWidget(self.power_button)

    def speed(self):
        try:
            distance = float(self.distance_input.text())
            time = float(self.time_input.text())
            speed = distance / time
            self.speed_result.setText(f"Speed: {speed} m/s")
        except ValueError:
            self.speed_result.setText("Error: Please enter valid numbers")

    def acceleration(self):
        try:
            initial_speed = float(self.initial_speed_input.text())
            final_speed = float(self.final_speed_input.text())
            time = float(self.accel_time_input.text())
            acceleration = (final_speed - initial_speed) / time
            self.acceleration_result.setText(f"Acceleration: {acceleration} m/s²")
        except ValueError:
            self.acceleration_result.setText("Error: Please enter valid numbers")

    def density(self):
        try:
            mass = float(self.mass_input.text())
            volume = float(self.volume_input.text())
            density = mass / volume
            self.density_result.setText(f"Density: {density} kg/m³")
        except ValueError:
            self.density_result.setText("Error: Please enter valid numbers")

    def power(self):
        try:
            force = float(self.force_input.text())
            speed = float(self.power_speed_input.text())
            power = force * speed
            self.power_result.setText(f"Power: {power} W")
        except ValueError:
            self.power_result.setText("Error: Please enter valid numbers")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CalcApp()
    main_window.show()
    sys.exit(app.exec_())
