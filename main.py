from diaries.DiarySample import DiarySample
from diaries.NaikiDiary import NaikiDiary
from diaries.TsutsuiDiary import TsutsuiDiary
# 下のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           TsutsuiDiary(),
           NaikiDiary()
           ]

for d in diaries:
    print("------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
