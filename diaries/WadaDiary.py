from diaries.AbstractDiary import AbstractDiary

class WadaDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-12-09"
    
    def get_summary(self):
        return "オブジェクト指向プログラミングでのチーム開発初日"
    
    def get_author(self):
        return "Wada"