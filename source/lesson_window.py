from PySide2 import QtWidgets, QtGui, QtCore
import sys
from source.lesson import Lesson, LessonNote, LessonState


class LessonWindow(QtWidgets.QWidget):
    notes = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF"]

    def __init__(self):
        super().__init__()
        self.__set_gui_properties()
        self.__create_gui_widgets()
        self.__create_gui_layouts()
        self.__apply_gui_layouts()

    def __set_gui_properties(self):
        self.setWindowTitle("Lesson Adder")
        self.setFixedSize(650, 250)
        self.text_font = QtGui.QFont("Tahoma", 10)
        self.text_font.setBold(True)
        self.label_size = QtCore.QSize(300, 25)

    def __create_gui_widgets(self):
        self.lesson_code_label = QtWidgets.QLabel("Lesson Code: ")
        self.lesson_code_label.setFixedSize(self.label_size)
        self.lesson_code_label.setFont(self.text_font)

        self.lesson_code_in = QtWidgets.QLineEdit()
        self.lesson_code_in.setFixedSize(self.label_size)
        self.lesson_code_in.setFont(self.text_font)

        self.lesson_credit_label = QtWidgets.QLabel("Lesson Credit: ")
        self.lesson_credit_label.setFixedSize(self.label_size)
        self.lesson_credit_label.setFont(self.text_font)

        self.lesson_credit_in = QtWidgets.QSpinBox()
        self.lesson_credit_in.setFixedSize(self.label_size)
        self.lesson_credit_in.setFont(self.text_font)
        self.lesson_credit_in.setMinimum(0)
        self.lesson_credit_in.setSingleStep(1)

        self.lesson_note_label = QtWidgets.QLabel("Lesson Note: ")
        self.lesson_note_label.setFixedSize(self.label_size)
        self.lesson_note_label.setFont(self.text_font)

        self.lesson_note_in = QtWidgets.QComboBox()
        self.lesson_note_in.setFixedSize(self.label_size)
        self.lesson_note_in.setFont(self.text_font)
        self.lesson_note_in.addItems(self.notes)

        self.lesson_state_in = QtWidgets.QCheckBox("Previously Taken")
        self.lesson_state_in.setFixedSize(self.label_size)
        self.lesson_state_in.setFont(self.text_font)
        self.lesson_state_in.stateChanged.connect(self.__state_change_prev)

        self.finish_button = QtWidgets.QPushButton("Finish")
        self.finish_button.setFixedSize(self.label_size)
        self.finish_button.setFont(self.text_font)

        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.setFixedSize(self.label_size)
        self.cancel_button.setFont(self.text_font)
        self.cancel_button.clicked.connect(self.close)

    def __create_gui_layouts(self):
        self.formBox = QtWidgets.QFormLayout()
        self.vMainBox = QtWidgets.QVBoxLayout()

    def __apply_gui_layouts(self):
        self.formBox.addRow(self.lesson_code_label, self.lesson_code_in)
        self.formBox.addRow(self.lesson_credit_label, self.lesson_credit_in)
        self.formBox.addRow(self.lesson_note_label, self.lesson_note_in)

        self.vMainBox.addStretch()
        self.vMainBox.addLayout(self.formBox)
        self.vMainBox.addWidget(self.lesson_state_in)
        self.vMainBox.addWidget(self.finish_button)
        self.vMainBox.addWidget(self.cancel_button)
        self.vMainBox.addStretch()

        self.setLayout(self.vMainBox)

    def __create_prev_row(self):
        self.lesson_prev_note_label = QtWidgets.QLabel("Lesson Previous Note: ")
        self.lesson_prev_note_label.setFixedSize(self.label_size)
        self.lesson_prev_note_label.setFont(self.text_font)

        self.lesson_prev_note_in = QtWidgets.QComboBox()
        self.lesson_prev_note_in.setFixedSize(self.label_size)
        self.lesson_prev_note_in.setFont(self.text_font)
        self.lesson_prev_note_in.addItems(self.notes)

    def __state_change_prev(self):
        if self.lesson_state_in.isChecked():
            self.__create_prev_row()
            self.formBox.addRow(self.lesson_prev_note_label, self.lesson_prev_note_in)
        else:
            self.formBox.removeRow(self.formBox.rowCount() - 1)

    def get_lesson(self):
        if self.lesson_state_in.isChecked():
            return Lesson(self.lesson_code_in.text(), int(self.lesson_credit_in.text()), self.lesson_note_in.currentText(),
                          LessonState.Old, self.lesson_prev_note_in.currentText())
        else:
            return Lesson(self.lesson_code_in.text(), self.lesson_credit_in.value(), self.lesson_note_in.currentText(),
                          LessonState.New)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LessonWindow()
    window.show()
    sys.exit(app.exec_())
