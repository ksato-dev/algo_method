# -*- coding: utf-8 -*-
import re
if __name__ == "__main__":
    input_str = input()
    reg_str = r"ru(?=r)"  # ru の後に r が続くパターンを探す正規表現
    ans_str = re.sub(reg_str, "ra", input_str)  # ru を見つけるので ra で置き換える。
    print(ans_str)
