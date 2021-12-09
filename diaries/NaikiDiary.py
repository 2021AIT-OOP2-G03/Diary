from diaries.AbstractDiary import AbstractDiary


class NaikiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "非常に大変でした。。"

    def get_author(self):
        return "Naiki"
