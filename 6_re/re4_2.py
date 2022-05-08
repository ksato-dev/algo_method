# -*- coding: utf-8 -*-
import re
if __name__ == "__main__":
    input_str = input()

    # asian の後に（スペース ＋ 英小文字）が５回連続で続くパターンを探す正規表現
    reg_str = r"asian(?=( [a-z]+){5,})"

    ans_str = re.sub(reg_str, "global", input_str)
    print(ans_str)
