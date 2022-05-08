# -*- coding: utf-8 -*-
import re
if __name__ == "__main__":
    input_str = input()

    # rithm または method ではない５文字以上の英小文字を
    # ポストフィックスとして持つ algo を探す。
    reg_str = r"algo(?!(rithm|method))[a-z]{5,}"

    if re.search(reg_str, input_str):
        print("Yes")
    else:
        print("No")
