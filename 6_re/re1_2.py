# -*- coding: utf-8 -*-
import re
if __name__ == "__main__":
    input_str = input()
    ans_str = "No"
    reg_str = r"^methoo*d$"
    searched_result = re.search(reg_str, input_str)
    if searched_result:
        ans_str = "Yes"
    print(ans_str)
