from diaries.AbstractDiary import AbstractDiary

class TakamuraDiary(AbstractDiary):
    def get_date(self):
        return "2021_12-09"

    def get_summary(self):
        return "初回のグループワークでした。gitのコマンドは使ったことがあったのですが、desktopの方は初めてでした。覚えます…よろしくお願いします"
    
    def get_author(self):
        return "Takamura"