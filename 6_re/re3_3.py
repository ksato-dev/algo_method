# -*- coding: utf-8 -*-
import re
if __name__ == "__main__":
    input_str = input()
    ans_str = "No"
    reg_str = r"^(\d{3,3})\-(\d{4,4})$"
    if re.match(reg_str, input_str):
        ans_str = "Yes"
    print(ans_str)
