from diaries.AbstractDiary import AbstractDiary


class SakuramotoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "良い日だった"

    def get_author(self):
        return "Sakuramoto"