from PySide2 import QtWidgets, QtGui, QtCore

from source.backend import Backend
from source.lesson import LessonState
from source.lesson_window import LessonWindow


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.backend = Backend()
        self.__set_gui_properties()
        self.__create_gui_widgets()
        self.__create_gui_layouts()
        self.__apply_gui_layouts()

    def __set_gui_properties(self):

        self.setWindowTitle("University Note Calculator")
        self.setFixedSize(650, 500)
        self.text_font = QtGui.QFont("Tahoma", 10)
        self.text_font.setBold(True)
        self.label_size = QtCore.QSize(300, 25)
        self.button_size = QtCore.QSize(100, 25)
        self.label_size_wide = QtCore.QSize(600, 25)

    def __create_gui_widgets(self):

        self.lesson_widget = None

        self.current_note_label = QtWidgets.QLabel("Current Note: ")
        self.current_note_label.setFixedSize(self.label_size)
        self.current_note_label.setFont(self.text_font)

        self.current_note_in = QtWidgets.QLineEdit()
        self.current_note_in.setFixedSize(self.label_size)
        self.current_note_in.setFont(self.text_font)

        self.current_credit_label = QtWidgets.QLabel("Current Credit: ")
        self.current_credit_label.setFixedSize(self.label_size)
        self.current_credit_label.setFont(self.text_font)

        self.current_credit_in = QtWidgets.QSpinBox()
        self.current_credit_in.setFixedSize(self.label_size)
        self.current_credit_in.setFont(self.text_font)
        self.current_credit_in.setMinimum(0)
        self.current_credit_in.setMaximum(10000000)
        self.current_credit_in.setSingleStep(1)

        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Lesson Code", "Credit", "Note", "Previous Note"])
        self.table_widget.setFont(self.text_font)
        self.table_widget.setColumnWidth(0, 200)
        self.table_widget.setColumnWidth(1, 100)
        self.table_widget.setColumnWidth(2, 100)
        self.table_widget.setColumnWidth(3, 100)

        self.new_note_label = QtWidgets.QLabel("New Note: ")
        self.new_note_label.setFixedSize(self.label_size)
        self.new_note_label.setFont(self.text_font)

        self.add_lesson_button = QtWidgets.QPushButton("Add Lesson")
        self.add_lesson_button.setFixedSize(self.button_size)
        self.add_lesson_button.setFont(self.text_font)
        self.add_lesson_button.clicked.connect(self.__open_lesson_widget)

        self.calc_button = QtWidgets.QPushButton("Calculate")
        self.calc_button.setFixedSize(self.button_size)
        self.calc_button.setFont(self.text_font)
        self.calc_button.clicked.connect(self.__calculate_note)

        self.reset_button = QtWidgets.QPushButton("Reset")
        self.reset_button.setFixedSize(self.button_size)
        self.reset_button.setFont(self.text_font)
        self.reset_button.clicked.connect(self.__reset_lessons)

        self.del_button = QtWidgets.QPushButton("Delete Row")
        self.del_button.setFixedSize(self.button_size)
        self.del_button.setFont(self.text_font)
        self.del_button.clicked.connect(self.__delete_lesson)

    def __reset_table(self):
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Lesson Code", "Credit", "Note", "Previous Note"])
        self.table_widget.setFont(self.text_font)
        self.table_widget.setColumnWidth(0, 200)
        self.table_widget.setColumnWidth(1, 100)
        self.table_widget.setColumnWidth(2, 100)
        self.table_widget.setColumnWidth(3, 100)

    def __create_gui_layouts(self):
        self.formBox = QtWidgets.QFormLayout()
        self.hBox = QtWidgets.QHBoxLayout()
        self.vMainBox = QtWidgets.QVBoxLayout()

    def __apply_gui_layouts(self):
        self.formBox.addRow(self.current_note_label, self.current_note_in)
        self.formBox.addRow(self.current_credit_label, self.current_credit_in)

        self.hBox.addStretch()
        self.hBox.addWidget(self.add_lesson_button)
        self.hBox.addWidget(self.calc_button)
        self.hBox.addWidget(self.del_button)
        self.hBox.addWidget(self.reset_button)
        self.hBox.addStretch()

        self.vMainBox.addStretch()
        self.vMainBox.addLayout(self.formBox)
        self.vMainBox.addWidget(self.table_widget)
        self.vMainBox.addWidget(self.new_note_label)
        self.vMainBox.addLayout(self.hBox)
        self.vMainBox.addStretch()

        self.setLayout(self.vMainBox)

    def __add_lesson(self):
        lesson = self.lesson_widget.get_lesson()
        self.backend.lessons.append(lesson)
        row = self.table_widget.rowCount()
        self.table_widget.insertRow(row)
        self.table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(lesson.code))
        self.table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(lesson.credit)))
        self.table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(lesson.note))
        if lesson.state == LessonState.Old:
            self.table_widget.setItem(row, 3, QtWidgets.QTableWidgetItem(lesson.prev_note))
        else:
            self.table_widget.setItem(row, 3, QtWidgets.QTableWidgetItem("New Credit"))
        self.lesson_widget.close()

    def __open_lesson_widget(self):
        self.lesson_widget = LessonWindow()
        self.lesson_widget.finish_button.clicked.connect(self.__add_lesson)
        self.lesson_widget.show()

    def __reset_lessons(self):
        self.table_widget.clear()
        self.table_widget.setRowCount(0)
        self.__reset_table()
        self.backend.lessons.clear()
        self.new_note_label.setText("New Note: ")
        self.current_credit_in.clear()
        self.current_note_in.clear()

    def __calculate_note(self):
        self.backend.general_note = float(self.current_note_in.text())
        self.backend.taken_credits = int(self.current_credit_in.text())
        self.new_note_label.setText(f"New Note: {self.backend.calculate_new_note()} ")

    def __delete_lesson(self):
        if self.table_widget.currentRow() != -1:
            self.backend.lessons.pop(self.table_widget.currentRow())
            self.table_widget.removeRow(self.table_widget.currentRow())
