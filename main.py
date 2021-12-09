from diaries.DiarySample import DiarySample
from diaries.MatsuiDiary import MatsuiDiary
from diaries.NaikiDiary import NaikiDiary
from diaries.SakuramotoDiary import SakuramotoDiary
from diaries.TakamuraDiary import TakamuraDiary
from diaries.UjiieDiary import UjiieDiary
from diaries.TsutsuiDiary import TsutsuiDiary
from diaries.WadaDiary import WadaDiary

# 下のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MatsuiDiary(), 
    NaikiDiary(),
    SakuramotoDiary(),
    TakamuraDiary(), 
    UjiieDiary(),
    TsutsuiDiary(),
    WadaDiary(),
]

for d in diaries:
    print("------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
