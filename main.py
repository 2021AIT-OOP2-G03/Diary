from diaries.DiarySample import DiarySample
from diaries.TakamuraDiary import TakamuraDiary
from diaries.UjiieDiary import UjiieDiary
from diaries.TsutsuiDiary import TsutsuiDiary
from diaries.WadaDiary import WadaDiary

# 下のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    TakamuraDiary()
    DiarySample(), 
    UjiieDiary(),
    WadaDiary(),
    TsutsuiDiary(),
]

for d in diaries:
    print("------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
