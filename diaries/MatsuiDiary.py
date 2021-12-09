from diaries.AbstractDiary import AbstractDiary

class MatsuiDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-12-09"
    
    def get_summary(self):
        return "作業量が多くて焦った。"
    
    def get_author(self):
        return "Matsui"