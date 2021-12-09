from diaries.DiarySample import DiarySample
from diaries.SakuramotoDiary import SakuramotoDiary

# 下のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    SakuramotoDiary(),
    ]

for d in diaries:
    print("------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()