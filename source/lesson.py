from strenum import StrEnum


class LessonState(StrEnum):
    New: str = "New"
    Old: str = "Old"


class LessonNote(StrEnum):
    AA: str = "AA"
    BA: str = "BA"
    BB: str = "BB"
    CB: str = "CB"
    CC: str = "CC"
    DC: str = "DC"
    DD: str = "DD"
    FF: str = "FF"

    @classmethod
    def get_note(cls, state):
        if state == cls.AA:
            return 4.0
        elif state == cls.BA:
            return 3.5
        elif state == cls.BB:
            return 3.0
        elif state == cls.CB:
            return 2.5
        elif state == cls.CC:
            return 2.0
        elif state == cls.DC:
            return 1.5
        elif state == cls.DD:
            return 1.0
        elif state == cls.FF:
            return 0.0


class Lesson:

    def __init__(self, code: str, credit: int, note: LessonNote, state: LessonState, prev_note: LessonNote = LessonNote.FF):
        self.code = code
        self.credit = credit
        self.note = note
        self.state = state
        self.prev_note = prev_note
