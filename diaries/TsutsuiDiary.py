from diaries.AbstractDiary import AbstractDiary


class  TsutsuiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-08"

    def get_summary(self):
        return "自作パソコンの配線整理をした。せっかくプラグイン式にしたのに配線が汚いのはみっともない。"

    def get_author(self):
        return "Shota Tsutsui"
