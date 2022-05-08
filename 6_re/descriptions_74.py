# 正規表現を取り扱うためのライブラリ

import re


# 調べたい文字列

S = 'algomethod'

# 調べる正規表現

reg = r'^a.*d$'


# マッチした位置が格納される (存在しなければ null)

search = re.search(reg, S)

if search:

    # "Yes" と表示される

    print("Yes")

else:

    print("No")
