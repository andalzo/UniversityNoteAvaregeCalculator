from source.lesson import *


class Backend:

    def __init__(self):
        self.lessons = list()
        self.general_note = None
        self.taken_credits = None

    @staticmethod
    def __change_from_new_lesson(lesson):
        return lesson.credit * LessonNote.get_note(lesson.note)

    @staticmethod
    def __change_from_old_lesson(lesson):
        return (LessonNote.get_note(lesson.note) - LessonNote.get_note(lesson.prev_note)) * lesson.credit

    def __calculate_changes(self):
        self.__new_credit = 0
        self.__change = 0
        for lesson in self.lessons:
            if lesson.state == LessonState.New:
                self.__change += self.__change_from_new_lesson(lesson)
                self.__new_credit += lesson.credit
            elif lesson.state == LessonState.Old:
                self.__change += self.__change_from_old_lesson(lesson)
            else:
                print("Error: This is not possible!")

    def calculate_new_note(self) -> float:
        old_total_note = self.general_note * self.taken_credits
        self.__calculate_changes()
        new_old_total_note = old_total_note + self.__change
        return new_old_total_note / (self.taken_credits + self.__new_credit)
