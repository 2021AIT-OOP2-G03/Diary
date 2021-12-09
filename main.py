from diaries.DiarySample import DiarySample
from diaries.TsutsuiDiary import TsutsuiDiary
from diaries.WadaDiary import WadaDiary

# 下のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           WadaDiary(),
           TsutsuiDiary(),
           ]

for d in diaries:
    print("------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
