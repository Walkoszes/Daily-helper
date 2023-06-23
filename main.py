#import all clases and function from the module
from PyQt5.QtWidgets import *
#imports modules, QtCore - provides core non-GUI functionality, such as event handling, and application settings
#QtGui - contains classes for handling graphical elements, such as windows, widgets, buttons, labels, and images
#QtWidgets - includes a set of UI elements (widgets) that can be used to build the GUI, such as buttons, checkboxes, layouts etc.
#uic - stands for User Interface Compiler, which allows loading and using UI files created with Qt Designer to construct the GUI layout
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#import QPixmap class, from the Pyqt5.QtGui module, this class provides functionality for working with images and pixmaps in PyQt5
from PyQt5.QtGui import QPixmap
#import class from the "password_window_ui" module
from password_window_ui import Ui_SecondWindow
#import class from the "Cal_bmi_window_ui" module
from Cal_bmi_window_ui import Ui_Cal_bmi_window
#import class from the "Note_window_ui" module
from Notes_window_ui import Ui_MainWindow
#import module, which provides various functions and variables that are used to manipulate different parts of the Python runtime environment
import sys
#import module, which contains functions for working with JSON data
import json
#module import, which interacts with the operating system for tasks like file and directory manipulation, command execution, and more
import os
#module import, which provides functions for working with file paths and directories
import os.path
#import function, which randomly selects an element from a sequence.
from random import choice

#CSS was used in this code and in the ui/modules files. They are tagged

#provides the basic functionality and appearance of the application's main window and of the functionality of the plan program
class UI(QMainWindow):
    #initialize the "UI" object by invoking the initialization logic of its superclass
    def __init__(self):
        super(UI, self).__init__()
        #set window title
        self.title = "Daily Helper"
        self.setWindowTitle(self.title)

        # Installing images
        self.picture1 = QLabel(self)
        self.picture2 = QLabel(self)
        self.pixmap = QPixmap('ornament.png')

        # Scale the pixmap to fit the specified sizes and set the posision
        self.picture1.setGeometry(10, -10, 61, 412)
        self.picture2.setGeometry(630, -10, 61, 412)
        self.pixmap = self.pixmap.scaled(61, 412)

        self.picture1.setPixmap(self.pixmap)
        self.picture2.setPixmap(self.pixmap)

        # Load the ui file
        uic.loadUi("qtdes_pr.ui", self)

        # Connect buttons to their functions
        self.add_p.clicked.connect(self.add_checkbox_lineedit)
        self.delete_p.clicked.connect(self.delete_checkbox_lineedit)
        self.b_password.clicked.connect(self.open_second_window)
        self.b_cal_bmi.clicked.connect(self.open_third_window)
        self.b_notes.clicked.connect(self.open_forth_window)
        self.inv_b.clicked.connect(self.open_fifth_window)

        # Create the QLabel widget for "kashtan" image, set the posision
        self.kashtan_label = QLabel(self)
        self.kashtan_pixmap = QPixmap('kashtan.png')
        self.kashtan_label.setGeometry(470, 260, 800, 800)
        self.kashtan_label.setPixmap(self.kashtan_pixmap)
        self.kashtan_label.setScaledContents(True)
        self.kashtan_label.setMouseTracking(True)
        self.kashtan_label.enterEvent = self.kashtan_enter_event
        self.kashtan_label.leaveEvent = self.kashtan_leave_event

        # Initialize a counter to keep track of the number of pairs of checkboxes and lineedits
        self.pair_counter = 0

        # Create a list to store the checkbox and line edit pairs
        self.checkbox_lineedit_pairs = []

        # Set the initial minimum height for the window
        self.setMinimumHeight(380)

        # Show the app
        self.show()

    #method that provides only shows the action taken when the mouse enters the widget
    def kashtan_enter_event(self, event):
        # event - the event object provides information about the mouse entering the widget
        self.kashtan_label.setPixmap(QPixmap('kashtan2.png'))

    #method is responsible for updating the pixmap of the kashtan_label widget by setting it to the original image ('kashtan.png') when the mouse cursor moves out of the widget's area
    def kashtan_leave_event(self, event):
        # event - the event object provides information about the mouse leaving the widget
        self.kashtan_label.setPixmap(QPixmap('kashtan.png'))

    #method that proveides ensures proper UI display and positioning across different window sizes
    def resizeEvent(self, event):
        #event - helps adjust UI elements based on the new window size

        global width_scale
        global height_scale

        # Get the new size of the window
        new_size = event.size()

        # Calculate the scaling factor based on the new size and the original size of the window
        width_scale = new_size.width() / 687  # Original width of the window is 687
        height_scale = new_size.height() / 412  # Original height of the window is 412

        # Resize and move the widgets according to the scaling factor
        self.l_tools.setGeometry(QtCore.QRect(int(81 * width_scale), int(11 * height_scale), int(107 * width_scale), int(21 * height_scale)))
        self.l_plans.setGeometry(QtCore.QRect(int(80 * width_scale), int(170 * height_scale), int(145 * width_scale), int(21 * height_scale)))

        self.list.setGeometry(QtCore.QRect(int(80 * width_scale), int(40 * height_scale), int(131 * width_scale), int(121 * height_scale)))
        self.calendar.setGeometry(QtCore.QRect(int(240 * width_scale), int(10 * height_scale), int(391 * width_scale), int(241 * height_scale)))

        self.b_cal_bmi.setGeometry(QtCore.QRect(int(81 * width_scale), int(41 * height_scale), int(129 * width_scale), int(25 * height_scale)))
        self.b_notes.setGeometry(QtCore.QRect(int(81 * width_scale), int(73 * height_scale), int(129 * width_scale), int(25 * height_scale)))
        self.b_password.setGeometry(QtCore.QRect(int(81 * width_scale), int(104 * height_scale), int(129 * width_scale), int(25 * height_scale)))
        self.inv_b.setGeometry(QtCore.QRect(int(81 * width_scale), int(136 * height_scale), int(129 * width_scale), int(25 * height_scale)))
        self.add_p.setGeometry(QtCore.QRect(int(80 * width_scale), int(200 * height_scale), int(141 * width_scale), int(28 * height_scale)))
        self.delete_p.setGeometry(QtCore.QRect(int(80 * width_scale), int(230 * height_scale), int(141 * width_scale), int(28 * height_scale)))

        self.kashtan_label.setGeometry(QtCore.QRect(int(470 * width_scale), int(260* height_scale), int(800* width_scale), int(800* height_scale)))
        self.picture1.setGeometry(int(10 * width_scale), int(-10 * height_scale), int(61* height_scale), int(412 * height_scale))
        self.picture2.setGeometry(int(630 * width_scale), int(-10 * height_scale), int(61* height_scale), int(412 * height_scale))
        self.pixmap = self.pixmap.scaled(int(61* height_scale), int(412 * height_scale))
        self.picture1.setPixmap(self.pixmap)
        self.picture2.setPixmap(self.pixmap)

        for checkbox, lineedit in self.checkbox_lineedit_pairs:
            x = int(81 * width_scale)  # Adjust the x-coordinate based on the scaling factor
            y = int(200 * height_scale) + (30 * self.checkbox_lineedit_pairs.index((checkbox, lineedit)))  # Adjust the y-coordinate based on the scaling factor and the index

            # Resize and move the checkbox
            checkbox.setGeometry(x, y, int(16 * width_scale), int(16 * height_scale))

            # Resize and move the line edit
            lineedit.setGeometry(x + int(29 * width_scale), y, int(109 * width_scale), int(22 * height_scale))

            delete_p_y = int(self.delete_p.y() * height_scale) + int(30*height_scale)

            self.add_p.move(int(self.add_p.x() * width_scale), int((self.add_p.y() + 30) * height_scale))
            self.delete_p.move(int(self.delete_p.x() * width_scale), int(delete_p_y * height_scale))

        # Call the base class resizeEvent function
        super().resizeEvent(event)

    #function adds a new checkbox and line edit pair to the main window
    def add_checkbox_lineedit(self):
        #allow the user to dynamically add checkbox and line edit pairs to the main window
        if self.pair_counter < 5:
            # Create a new checkbox and line edit
            checkbox = QCheckBox(self) #creating new checkbox
            lineedit = QLineEdit(self) #creating new line_edit

            # Calculate the position of the new checkbox and lineedit pair based on the counter
            x = int(81 * width_scale) #set the x coordination for checkboxes and line_edits
            y = int(200 * height_scale) + (30  * self.pair_counter) #calculating new y for every checkbox and line_edit

            # Set the properties of the checkbox
            checkbox.setGeometry(x, y, int(16*width_scale), int(16*height_scale))

            # Set the properties of the line edit
            lineedit.setGeometry(x + 29, y, int(109*width_scale), int(22*height_scale))

            # Add the checkbox and line edit to the main window
            checkbox.show()
            lineedit.show()

            # Append the checkbox and line edit pair to the list (checkbox_lineedit_pairs)
            self.checkbox_lineedit_pairs.append((checkbox, lineedit))

            # Increase the pair counter
            self.pair_counter = self.pair_counter + 1

            # Calculate the new position of the "delete_p" button
            delete_p_y = self.delete_p.y() + 30

            # Move the buttons down
            self.add_p.move(self.add_p.x(), self.add_p.y() + 30)
            self.delete_p.move(self.delete_p.x(), delete_p_y)
        else:
            #if the max amount of the checkboxes and line_edits was reached
            QMessageBox.warning(self, "Maximum Limit Reached", "You can only add up to 5 plans")

    #method that allows the user to delete selected/checked checkbox and line edit pairs from the main window
    def delete_checkbox_lineedit(self):
        # Check if any checkbox is checked
        if any(checkbox.isChecked() for checkbox, _ in self.checkbox_lineedit_pairs):
            # Create a list to store the remaining checkbox and line edit pairs
            remaining_pairs = []

            # Iterate through the checkbox and line edit pairs
            for checkbox, lineedit in self.checkbox_lineedit_pairs:
                # Check if the checkbox is checked
                if not checkbox.isChecked():
                    # Add the checkbox and line edit pair to the remaining pairs list
                    remaining_pairs.append((checkbox, lineedit))
                else:
                    # Remove the checkbox and line edit from the main window
                    checkbox.deleteLater()
                    lineedit.deleteLater()

            #loop that allows safe deletion of checkboxes and line_edits pairs from the self.checkbox_lineedit_pairs list by iterating in reverse order
            for i in range(len(self.checkbox_lineedit_pairs) - 1, -1, -1):
                checkbox, lineedit = self.checkbox_lineedit_pairs[i]

                # Check if the checkbox is checked
                if checkbox.isChecked():
                    # Remove the checkbox and line edit from the main window
                    checkbox.deleteLater()
                    lineedit.deleteLater()

                    # Delete the checkbox and line edit pair from the list
                    self.checkbox_lineedit_pairs.pop(i)

                    # Decrease the pair counter
                    self.pair_counter = self.pair_counter - 1

            # Update the checkbox and line edit pairs list with the remaining pairs
            self.checkbox_lineedit_pairs = remaining_pairs

            # Calculate the new y-coordinate for the buttons
            button_y = 200 + (30 * len(self.checkbox_lineedit_pairs))

            # Move the buttons up
            self.add_p.move(self.add_p.x(), button_y + 5)
            self.delete_p.move(self.delete_p.x(), button_y + 35)

            # Update the positions of the remaining checkbox and line edit pairs
            for i, (checkbox, lineedit) in enumerate(self.checkbox_lineedit_pairs):
                y = 200 + (30 * i)
                checkbox.move(checkbox.x(), y)
                lineedit.move(lineedit.x(), y)
        else:
            #if nothing checked and the user click on the button "delete_b"
            QMessageBox.warning(self, "No Checkbox Selected", "Please select a checkbox to delete.")

    #method method creates and shows an instance of the SecondWindow class, allowing the user to interact with it separately from the main window
    def open_second_window(self):
            self.second_window = SecondWindow()
            self.second_window.show()

    #method method creates and shows an instance of the ThrirdWindow class, allowing the user to interact with it separately from the main window
    def open_third_window(self):
            self.third_window = ThirdWindow()
            self.third_window.show()

    #method method creates and shows an instance of the ForthWindow class, allowing the user to interact with it separately from the main window
    def open_forth_window(self):
                self.forth_window = ForthWindow()
                self.forth_window.show()

    #method method creates and shows an instance of the FifthWindow class, allowing the user to interact with it separately from the main window
    def open_fifth_window(self):
            self.fifth_window = FifthWindow()
            self.fifth_window.show()

#responsible for managing the functionality and appearance of the second window of the application and of the functioanality of the password program
#Multiple application
class SecondWindow(QMainWindow):
    #__init__ method of SecondWindow initializes the window and sets up the user interface using Ui_SecondWindow
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)

        # Scale the pixmap to fit the specified sizes and set the posision
        self.picture1 = QLabel(self)
        self.pixmap = QPixmap('ornament.png')
        self.picture1.setGeometry(0, -10, 61, 412)
        self.picture1.setPixmap(self.pixmap)

        # Connect the "Generate" button to the password generation function
        self.ui.generate_b.clicked.connect(self.generate_password)
    #method that creates a password based on the user's checkbox selections
    def generate_password(self):
        # checks if none of the checkboxes (num, ua, eng, symbols) are checked
        if not any([self.ui.num.isChecked(), self.ui.ua.isChecked(), self.ui.eng.isChecked(), self.ui.symbols.isChecked()]):
            #if nothing checked
            QMessageBox.warning(self, "Warning", "Please check at least one checkbox.")
            return

        elements = "" #used to store a combination of characters based on the selected checkboxes
        #builds the a string "elements" that contains the selected character sets based on the checked checkboxes
        if self.ui.num.isChecked():
            elements += "1234567890"
        if self.ui.eng.isChecked():
            elements += "ABCDEFGHIJKLMNOPQRSTU"
        if self.ui.ua.isChecked():
            elements += "ЙЦУКЕНГШЩЗХЇІФВАПРОЛДЖЄЯЧСМИТЬБЮ"
        if self.ui.symbols.isChecked():
            elements += "!@#$%^&*()_+=-./"


        password_length = self.ui.horizontalScrollBar.value() #assigned the current value of the horizontal scroll bar (horizontalScrollBar) in the "UI"

        # Generating the password
        result = "" #initialized as an empty string to store the generated password
        #loop is used to generate the password by randomly selecting characters from the elements string and appending them to the result string
        for _ in range(password_length):
            result += choice(elements)

        # Setting the password in the line edit
        self.ui.show_result.setText(result)

    #method that proveides ensures proper UI display and positioning across different window sizes
    def resizeEvent(self, event):
        #event - helps adjust UI elements based on the new window size

        # Get the new size of the window
        new_size = event.size()

        # Calculate the scaling factor based on the new size and the original size of the window
        width_scale = new_size.width() / 286  # Original width of the window is 687
        height_scale = new_size.height() / 273  # Original height of the window is 412

        # Resize and move the widgets according to the scaling factor
        self.ui.name.setGeometry(QtCore.QRect(int(51 * width_scale), int(11 * height_scale), int(220 * width_scale), int(21 * height_scale)))
        self.ui.pasword_l.setGeometry(QtCore.QRect(int(60 * width_scale), int(190 * height_scale), int(99 * width_scale), int(16 * height_scale)))
        self.ui.show_result.setGeometry(QtCore.QRect(int(51 * width_scale), int(48 * height_scale), int(221 * width_scale), int(22 * height_scale)))
        self.ui.eng.setGeometry(QtCore.QRect(int(52 * width_scale), int(78 * height_scale), int(107 * width_scale), int(20 * height_scale)))
        self.ui.ua.setGeometry(QtCore.QRect(int(52 * width_scale), int(105 * height_scale), int(120 * width_scale), int(20 * height_scale)))
        self.ui.symbols.setGeometry(QtCore.QRect(int(52 * width_scale), int(132 * height_scale), int(118 * width_scale), int(20 * height_scale)))
        self.ui.num.setGeometry(QtCore.QRect(int(52 * width_scale), int(159 * height_scale), int(82 * width_scale), int(20 * height_scale)))
        self.ui.horizontalScrollBar.setGeometry(QtCore.QRect(int(60 * width_scale), int(210 * height_scale), int(160 * width_scale), int(16 * height_scale)))
        self.ui.generate_b.setGeometry(QtCore.QRect(int(100 * width_scale), int(240 * height_scale), int(93 * width_scale), int(28 * height_scale)))
        self.ui.pas_length.setGeometry(QtCore.QRect(int(160 * width_scale), int(190 * height_scale), int(55 * width_scale), int(16 * height_scale)))

        self.picture1.setGeometry(int(0 * width_scale), int(-10 * height_scale), int(61* height_scale), int(412  * height_scale))
        self.pixmap = self.pixmap.scaled(int(61* height_scale), int(412  * height_scale))
        self.picture1.setPixmap(self.pixmap)

        # Call the base class resizeEvent function
        super().resizeEvent(event)

#responsible for managing the functionality and appearance of the third window, which is used for calculating BMI
#Multiple application
class ThirdWindow(QMainWindow):
    #initializes the ThirdWindow class and sets up its user interface using the Ui_Cal_bmi_window class
    def __init__(self):
        super(ThirdWindow, self).__init__()
        self.ui = Ui_Cal_bmi_window()
        self.ui.setupUi(self)

        # Set the coordinates and sizes of the ornament image
        self.picture1 = QLabel(self)
        self.pixmap = QPixmap('ornament.png')
        self.picture1.setGeometry(10, -10, 61, 412)
        self.picture1.setPixmap(self.pixmap)

        # Connect buttons to their functions
        self.ui.button_find.clicked.connect(self.nothing)
        self.ui.button_clearing.clicked.connect(self.clearing)
        self.ui.button_meaning.clicked.connect(self.show_meaning)

        self.result1 = "" #variable that is initialized as an empty string for future BMI number

        self.result_label = QLabel(self)  # Create a new QLabel for displaying the result
        self.result_label.setGeometry(145, 190, 55, 16)  # Adjust the position and size as needed
        self.result_label.setStyleSheet("font-size: 10pt; color: brown;")  # Adjust the font size and color #CSS using

    #function calculates and returns the rounded BMI based on the weight and height values entered
    def equaling(self):
        weight_num = int(self.ui.wrt_weight.text()) #assigned the integer value of the text entered in the wrt_weight field of the UI
        height_num = int(self.ui.wrt_height.text()) #assigned the integer value of the text entered in the wrt_height field of the UI
        equal = weight_num / ((height_num / 100) ** 2) #assigned the result of dividing weight_num by the square of height_num divided by 100
        equal = round(equal) #round to the nearest integer value
        return str(equal)

    #method checks if the text boxes for weight and height are empty. Otherwise, it calls the cal_bmi method.
    def nothing(self):
        text = self.ui.wrt_weight.text() #assigned the value entered in the wrt_weight text box
        text_2 = self.ui.wrt_height.text() #assigned the value entered in the wrt_height text box
        if text == "" or text_2 == "":
            QMessageBox.warning(self, "Error warning", "Please write numbers in the text box")
            return
        else:
            self.cal_bmi()

    #function calculates the BMI, handles input validation for whole numbers, and updates the result label
    def cal_bmi(self):
        text = self.ui.wrt_weight.text() #assigned the value entered in the wrt_weight text box
        text_2 = self.ui.wrt_height.text() #assigned the value entered in the wrt_height text box
        if any(not c.isdigit() for c in text) or any(not c.isdigit() for c in text_2):
            QMessageBox.warning(self, "Error warning", "You can write only whole numbers")
            return
        try:
            self.result1 = self.equaling() #assigned the result of the equaling function
            self.result_label.setText(self.result1)
        except ValueError:
            QMessageBox.warning(self, "Error warning", "You can write only whole numbers")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Error warning", "You can write only whole numbers")

    #clearing fields
    def clearing(self):
        self.ui.wrt_weight.clear()
        self.ui.wrt_height.clear()
        self.result_label.clear()

    #different messages based on the value of self.result1 to indicate the meaning or classification of their BMI
    def table_expl(self):
        if int(self.result1) >= 1 and int(self.result1) <= 15:
            msg_box = QMessageBox(self)
            self.title = "Meaning"
            msg_box.setWindowTitle(self.title)
            msg_box.setText("Low, you have dystrophy, very low weight")
            msg_box.exec_()
        if int(self.result1) >= 16 and int(self.result1) <= 18:
            msg_box = QMessageBox(self)
            self.title = "Meaning"
            msg_box.setWindowTitle(self.title)
            msg_box.setText("Average, deviation from the norm, but within the limits of age changes: you grow faster than you gain weight")
            msg_box.exec_()
        if int(self.result1) >= 18.5 and int(self.result1) <= 24.9:
            msg_box = QMessageBox(self)
            self.title = "Meaning"
            msg_box.setWindowTitle(self.title)
            msg_box.setText("Normal, your weight is normal")
            msg_box.exec_()
        if int(self.result1) >= 25 and int(self.result1) <= 30:
            msg_box = QMessageBox(self)
            self.title = "Meaning"
            msg_box.setWindowTitle(self.title)
            msg_box.setText("Average, deviation from the norm, but within the limits of age changes: you gain weight faster than you grow")
            msg_box.exec_()
        if int(self.result1) >= 30 and int(self.result1) <= 50 or int(self.result1) > 50:
            msg_box = QMessageBox(self)
            self.title = "Meaning"
            msg_box.setWindowTitle(self.title)
            msg_box.setText("High, you are obese, very heavy")
            msg_box.exec_()

    #method checks if self.result1 is empty and displays a warning message if it is, otherwise it calls the table_expl method
    def show_meaning(self):
        if not self.result1:
            QMessageBox.warning(self, "Error warning", "Calculate your BMI firstly")
        else:
            self.table_expl()

    #method that proveides ensures proper UI display and positioning across different window sizes
    def resizeEvent(self, event):
        #event - helps adjust UI elements based on the new window size
        # Get the new size of the window
        new_size = event.size()

        # Calculate the scaling factor based on the new size and the original size of the window
        width_scale = new_size.width() / 341  # Original width of the window is 687
        height_scale = new_size.height() / 262  # Original height of the window is 412

        # Resize and move the widgets according to the scaling factor
        self.ui.tool_name.setGeometry(QtCore.QRect(int(70 * width_scale), int(10 * height_scale), int(197 * width_scale), int(21 * height_scale)))
        self.ui.weight.setGeometry(QtCore.QRect(int(61 * width_scale), int(41 * height_scale), int(119 * width_scale), int(18 * height_scale)))
        self.ui.height.setGeometry(QtCore.QRect(int(61 * width_scale), int(69 * height_scale), int(122 * width_scale), int(18 * height_scale)))
        self.ui.result.setGeometry(QtCore.QRect(int(60 * width_scale), int(190 * height_scale), int(84 * width_scale), int(18 * height_scale)))
        self.result_label.setGeometry(QtCore.QRect(int(145 * width_scale), int(190 * height_scale), int(55 * width_scale), int(16 * height_scale)))

        self.ui.wrt_weight.setGeometry(QtCore.QRect(int(200 * width_scale), int(40 * height_scale), int(121 * width_scale), int(22 * height_scale)))
        self.ui.wrt_height.setGeometry(QtCore.QRect(int(200 * width_scale), int(69 * height_scale), int(121 * width_scale), int(22 * height_scale)))

        self.ui.button_clearing.setGeometry(QtCore.QRect(int(61 * width_scale), int(146 * height_scale), int(261 * width_scale), int(28 * height_scale)))
        self.ui.button_find.setGeometry(QtCore.QRect(int(61 * width_scale), int(106 * height_scale), int(261 * width_scale), int(28 * height_scale)))
        self.ui.button_meaning.setGeometry(QtCore.QRect(int(60 * width_scale), int(220 * height_scale), int(261 * width_scale), int(28 * height_scale)))

        self.picture1.setGeometry(int(10 * width_scale), int(-10 * height_scale), int(61* height_scale), int(412 * height_scale))
        self.pixmap = self.pixmap.scaled(int(61* height_scale), int(412 * height_scale))
        self.picture1.setPixmap(self.pixmap)

        # Call the base class resizeEvent function
        super().resizeEvent(event)

#responsible for managing the functionality and appearance of the fourth window, which is used for managing notes and files in the "Notes"application
#Multiple application
class ForthWindow(QMainWindow):
    #initializes the window and sets up the user interface using the Ui_MainWindow class
    def __init__(self):
        super(ForthWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set the coordinates and sizes of the ornament image
        self.picture1 = QLabel(self)
        self.pixmap = QPixmap('ornament.png')
        self.picture1.setGeometry(10, -10, 61, 412)
        self.picture1.setPixmap(self.pixmap)
        self.picture1.lower()

        # Instance variable to store the selected file name
        self.selected_file = ""

        # Load the list of file names from the JSON file
        self.file_list = []

        # Populate the list_files with the loaded file names
        self.ui.list_files.addItems(self.file_list)

        #called method
        self.load_file_list()

        # Connect buttons to their functions
        self.ui.save_b.clicked.connect(self.save_info)
        self.ui.save_changes.clicked.connect(self.save_edited_file)
        self.ui.del_note.clicked.connect(self.delete_file)
        self.ui.new_note.clicked.connect(self.clear_line_edit)
        self.ui.list_files.itemClicked.connect(self.open_file)

        # Create the QLabel widgets for "kashtan" image
        self.kashtan_label = QLabel(self)
        self.kashtan_pixmap = QPixmap('kashtan.png')
        self.kashtan_label.setGeometry(600, 10, 500, 500)
        self.kashtan_label.setPixmap(self.kashtan_pixmap)
        self.kashtan_label.setScaledContents(True)
        self.kashtan_label.setMouseTracking(True)
        self.kashtan_label.enterEvent = self.kashtan_enter_event
        self.kashtan_label.leaveEvent = self.kashtan_leave_event

    #method that provides only shows the action taken when the mouse enters the widget
    def kashtan_enter_event(self, event):
        # event - the event object provides information about the mouse entering the widget
        self.kashtan_label.setPixmap(QPixmap('kashtan2.png'))

    #method is responsible for updating the pixmap of the kashtan_label widget by setting it to the original image ('kashtan.png') when the mouse cursor moves out of the widget's area
    def kashtan_leave_event(self, event):
        # event - the event object provides information about the mouse leaving the widget
        self.kashtan_label.setPixmap(QPixmap('kashtan.png'))

    #method is responsible for saving the text entered in the wrtiting text edit to a file
    def save_info(self):
        text = self.ui.wrtiting.toPlainText() #retrieves the plain text content from the "wrtiting" text edit widget and assigns it to the variable "text"
        if text:
            # Prompt the user for a file name
            file_name, _ = QInputDialog.getText(self, "Save File", "Enter file name:")

            if file_name:
                # Set the path to the folder where the files will be saved
                folder_path = "info_folder"

                # Check if the folder exists, if not, create it
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Create the file path by joining the folder path and the file name
                file_path = os.path.join(folder_path, file_name)

                try:
                    # Open the file in write mode and save the text
                    with open(file_path, 'w') as file:
                        file.write(text)

                    # Show a success message
                    QMessageBox.information(self, "Info Saved", "Information saved successfully.")

                    # Add the file name to the QListWidget
                    self.ui.list_files.addItem(file_name)

                    # Add the file name to the list of file names
                    self.file_list.append(file_name)

                    # Save the updated list of file names to the JSON file
                    self.save_file_list()

                    # Clear the text edit
                    self.ui.wrtiting.clear()

                except OSError as e:
                    # Show an error message if there's an issue with saving the file
                    QMessageBox.critical(self, "Error", "An error occurred while saving the information.")
                    print(e)

    #loads the list of file names from the "info_folder" directory and populates the list_files with the file names
    def load_file_list(self):
        folder_path = "info_folder"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_list = os.listdir(folder_path) # retrieves the list of file names in the "info_folder" directory
        self.ui.list_files.clear()
        self.ui.list_files.addItems(file_list)

    #saves the list of file names (self.file_list) to a JSON file located at "file_list.json"
    def save_file_list(self):
        # Set the path to the JSON file storing the list of file names
        file_list_path = "file_list.json"

        # Save the list of file names to the JSON file
        with open(file_list_path, 'w') as file:
            json.dump(self.file_list, file)

    #method that,opens a file selected from a QListWidgetItem, reads its contents, and sets the file contents as the text in a QLineEdit
    def open_file(self, item):
        # Retrieve the selected file name from the QListWidgetItem
        file_name = item.text()

        # Set the path to the folder where the files are saved
        folder_path = "info_folder"

        # Create the file path by joining the folder path and the file name
        file_path = os.path.join(folder_path, file_name)

        try:
            # Open the file in read mode and read its contents
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Set the file contents as the text in the QLineEdit
            self.ui.wrtiting.setText(file_contents)

        except OSError as e:
            # Show an error message if there's an issue with opening the file
            QMessageBox.critical(self, "Error", "An error occurred while opening the file.")
            print(e)

    #method that deletes a file selected from the list by confirming with a message box
    def delete_file(self):
        # Check if an item is selected
        if self.ui.list_files.currentItem() is None:
            QMessageBox.warning(self, "Delete File", "No file selected.")
            return

        # Get the selected file name from the list
        selected_file = self.ui.list_files.currentItem().text()
        
        # Confirm the deletion with a message box
        reply = QMessageBox.question(self, "Delete File", f"Are you sure you want to delete '{selected_file}'?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # Delete the file
            folder_path = "info_folder"
            file_path = os.path.join(folder_path, selected_file)
            
            try:
                os.remove(file_path)
                self.ui.wrtiting.clear()
                self.ui.list_files.takeItem(self.ui.list_files.currentRow())  # Remove the item from the list
                QMessageBox.information(self, "Delete File", f"File '{selected_file}' has been deleted.")
            except OSError:
                QMessageBox.warning(self, "Delete File", f"Failed to delete file '{selected_file}'.")

    #method that updates the list of files displayed in the UI by retrieving the file list from a specific folder
    def update_file_list(self):
        folder_path = "info_folder"
        self.file_list = os.listdir(folder_path)
        self.ui.list_files.clear()
        self.ui.list_files.addItems(self.file_list)

    #method that clears the text in the "wrtiting" line edit widget, enables it, and sets the focus to it
    def clear_line_edit(self):
        self.ui.wrtiting.clear()
        self.ui.wrtiting.setEnabled(True)
        self.ui.wrtiting.setFocus()

    #method that saves the edited text in the line edit to the selected file, displaying a success message if the file exists and a warning message if the file does not exist
    def save_edited_file(self):
            # Check if an item is selected
            if self.ui.list_files.currentItem() is None:
                QMessageBox.warning(self, "Save File", "No file selected.")
                return

            # Get the selected file name from the list
            selected_file = self.ui.list_files.currentItem().text()

            # Construct the file path
            folder_path = "info_folder"
            file_path = os.path.join(folder_path, selected_file)

            # Check if the file exists
            if os.path.exists(file_path):
                # Get the edited text from the line edit
                edited_text = self.ui.wrtiting.toPlainText()

                # Save the edited text to the file
                with open(file_path, 'w') as file:
                    file.write(edited_text)

                QMessageBox.information(self, "Save File", f"File '{selected_file}' has been saved.")
            else:
                QMessageBox.warning(self, "Save File", f"File '{selected_file}' does not exist.")

    #method that proveides ensures proper UI display and positioning across different window sizes
    def resizeEvent(self, event):
        #event - helps adjust UI elements based on the new window size
        # Get the new size of the window
        new_size = event.size()

        # Calculate the scaling factor based on the new size and the original size of the window
        width_scale = new_size.width() / 716  # Original width of the window is 687
        height_scale = new_size.height() / 390  # Original height of the window is 412

        # Resize and move the widgets according to the scaling factor
        self.ui.l_note_name.setGeometry(QtCore.QRect(int(78 * width_scale), int(9 * height_scale), int(81 * width_scale), int(31 * height_scale)))
        self.ui.name_label.setGeometry(QtCore.QRect(int(70 * width_scale), int(80 * height_scale), int(81 * width_scale), int(21 * height_scale)))
        self.ui.list_files.setGeometry(QtCore.QRect(int(67 * width_scale), int(99 * height_scale), int(181 * width_scale), int(141 * height_scale)))
        self.ui.wrtiting.setGeometry(QtCore.QRect(int(267 * width_scale), int(99 * height_scale), int(431 * width_scale), int(281 * height_scale)))

        self.ui.new_note.setGeometry(QtCore.QRect(int(67 * width_scale), int(241 * height_scale), int(86 * width_scale), int(28 * height_scale)))
        self.ui.del_note.setGeometry(QtCore.QRect(int(161 * width_scale), int(241 * height_scale), int(86 * width_scale), int(28 * height_scale)))
        self.ui.save_b.setGeometry(QtCore.QRect(int(67 * width_scale), int(276 * height_scale), int(181 * width_scale), int(28 * height_scale)))
        self.ui.save_changes.setGeometry(QtCore.QRect(int(67 * width_scale), int(311 * height_scale), int(181 * width_scale), int(28 * height_scale)))

        self.kashtan_label.setGeometry(QtCore.QRect(int(600 * width_scale), int(10* height_scale), int(500* width_scale), int(500* height_scale)))
        self.picture1.setGeometry(int(10 * width_scale), int(-10 * height_scale), int(61* height_scale), int(412  * height_scale))
        self.pixmap = self.pixmap.scaled(int(61* height_scale), int(412  * height_scale))
        self.picture1.setPixmap(self.pixmap)

        # Call the base class resizeEvent function
        super().resizeEvent(event)

#provides the user interface and functionality for managing the inventory of products in the application
#Multiple application
class FifthWindow(QMainWindow):
    # initializes an instance of itself by invoking the method of it's superclass
    def __init__(self):
        super(FifthWindow, self).__init__()
        self.setWindowTitle("Inventory Management System")
        self.setGeometry(100, 100, 650, 390)  # Set window size and position

        # Scale the pixmap to fit the specified sizes and set the posision
        self.picture1 = QLabel(self)
        self.pixmap = QPixmap('ornament.png')
        self.picture1.setGeometry(10, -10, 61, 412)
        self.picture1.setPixmap(self.pixmap)

        # Create a Label for the title
        self.l_name = QLabel("Inventory Manage", self)
        self.l_name.setGeometry(61, -5, 580, 30)
        self.l_name.setStyleSheet("font-size: 18px; font-weight: bold;color : darkred; ") #CSS using

        # Create a table widget
        self.table_widget = QTableWidget(self) #using difficult widget(QTableWidget)
        self.table_widget.setGeometry(61, 20, 580, 300)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Product ID", "Product Name", "Quantity", "Price"])

        # Create line edits for entering product details
        self.id_line_edit = QLineEdit(self)
        self.id_line_edit.setGeometry(61, 330, 140, 25)
        self.id_line_edit.setPlaceholderText("Product ID")

        self.name_line_edit = QLineEdit(self)
        self.name_line_edit.setGeometry(201, 330, 140, 25)
        self.name_line_edit.setPlaceholderText("Product Name")

        self.quantity_line_edit = QLineEdit(self)
        self.quantity_line_edit.setGeometry(341, 330, 140, 25)
        self.quantity_line_edit.setPlaceholderText("Quantity")

        self.price_line_edit = QLineEdit(self)
        self.price_line_edit.setGeometry(481, 330, 140, 25)
        self.price_line_edit.setPlaceholderText("Price")

        # Create a button
        self.add_button = QPushButton("Add Product", self)
        self.add_button.setGeometry(61, 360, 93, 28)
        self.add_button.clicked.connect(self.add_product)

        self.delete_button = QPushButton("Delete Product", self)
        self.delete_button.setGeometry(154, 360, 93, 28)
        self.delete_button.clicked.connect(self.delete_product)

        self.save_button = QPushButton("Save Products", self)
        self.save_button.setGeometry(247, 360, 93, 28)
        self.save_button.clicked.connect(self.save_inventory)

        # Initialize the inventory data
        self.inventory = []

        # Load the inventory data
        self.load_inventory()

    #method adds a new product entry to the table widget based on the input values
    def add_product(self):
        product_id = self.id_line_edit.text()
        product_name = self.name_line_edit.text()
        quantity = self.quantity_line_edit.text()
        price = self.price_line_edit.text()

        if product_id and product_name and quantity and price:
            row_count = self.table_widget.rowCount()
            self.table_widget.insertRow(row_count)
            self.table_widget.setItem(row_count, 0, QTableWidgetItem(product_id))
            self.table_widget.setItem(row_count, 1, QTableWidgetItem(product_name))
            self.table_widget.setItem(row_count, 2, QTableWidgetItem(quantity))
            self.table_widget.setItem(row_count, 3, QTableWidgetItem(price))

            self.id_line_edit.clear()
            self.name_line_edit.clear()
            self.quantity_line_edit.clear()
            self.price_line_edit.clear()

    #method removes the selected rows from the table widget
    def delete_product(self):
        selected_rows = self.table_widget.selectedItems()
        if selected_rows:
            rows = set()
            for item in selected_rows:
                rows.add(item.row())
            for row in sorted(rows, reverse=True):
                self.table_widget.removeRow(row)

    #method saves the inventory data from the table widget to a file named "inventory.txt"
    def save_inventory(self):
        file_path = "inventory.txt"
        try:
            with open(file_path, 'w') as file:
                for row in range(self.table_widget.rowCount()):
                    product_id = self.table_widget.item(row, 0).text()
                    product_name = self.table_widget.item(row, 1).text()
                    quantity = self.table_widget.item(row, 2).text()
                    price = self.table_widget.item(row, 3).text()
                    line = f"{product_id},{product_name},{quantity},{price}\n"
                    file.write(line)
            QMessageBox.information(self, "Success", "Inventory saved successfully.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to save inventory: {str(e)}")

    #method reads the inventory data from the "inventory.txt" file
    def load_inventory(self):
        file_path = "inventory.txt"
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    product_id, product_name, quantity, price = line.strip().split(',')
                    row_count = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_count)
                    self.table_widget.setItem(row_count, 0, QTableWidgetItem(product_id))
                    self.table_widget.setItem(row_count, 1, QTableWidgetItem(product_name))
                    self.table_widget.setItem(row_count, 2, QTableWidgetItem(quantity))
                    self.table_widget.setItem(row_count, 3, QTableWidgetItem(price))
        except FileNotFoundError:
            # Handle the case where the file doesn't exist yet
            pass
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load inventory: {str(e)}")

    def resizeEvent(self, event):
        #event - helps adjust UI elements based on the new window size
        # Get the new size of the window
        new_size = event.size()

        # Calculate the scaling factor based on the new size and the original size of the window
        width_scale = new_size.width() / 650  # Original width of the window is 687
        height_scale = new_size.height() / 390  # Original height of the window is 412

        # Resize and move the widgets according to the scaling factor
        self.table_widget.setGeometry(QtCore.QRect(int(61 * width_scale), int(20 * height_scale), int(580 * width_scale), int(300 * height_scale)))
        self.l_name.setGeometry(QtCore.QRect(int(61 * width_scale), int(-5 * height_scale), int(580 * width_scale), int(30 * height_scale)))
        self.id_line_edit.setGeometry(QtCore.QRect(int(61 * width_scale), int(330 * height_scale), int(140 * width_scale), int(25 * height_scale)))
        self.name_line_edit.setGeometry(QtCore.QRect(int(201 * width_scale), int(330 * height_scale), int(140 * width_scale), int(25 * height_scale)))

        self.quantity_line_edit.setGeometry(QtCore.QRect(int(341 * width_scale), int(330 * height_scale), int(140 * width_scale), int(25 * height_scale)))
        self.price_line_edit.setGeometry(QtCore.QRect(int(481 * width_scale), int(330 * height_scale), int(140 * width_scale), int(25 * height_scale)))
        self.save_button.setGeometry(QtCore.QRect(int(247 * width_scale), int(360 * height_scale), int(93 * width_scale), int(28 * height_scale)))
        self.add_button.setGeometry(QtCore.QRect(int(61 * width_scale), int(360 * height_scale), int(93 * width_scale), int(28 * height_scale)))
        self.delete_button.setGeometry(QtCore.QRect(int(154 * width_scale), int(360 * height_scale), int(93 * width_scale), int(28 * height_scale)))

        self.picture1.setGeometry(int(10 * width_scale), int(-10 * height_scale), int(61* height_scale), int(412  * height_scale))
        self.pixmap = self.pixmap.scaled(int(61* height_scale), int(412  * height_scale))
        self.picture1.setPixmap(self.pixmap)

        # Call the base class resizeEvent function
        super().resizeEvent(event)

#sets up the main application window and starts the event loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())