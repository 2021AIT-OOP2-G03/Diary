from diaries.AbstractDiary import AbstractDiary

class UjiieDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-12-09"
    
    def get_summary(self):
        return "Githubの講義＋リーダー決め"
    
    def get_author(self):
        return "Ujiie"