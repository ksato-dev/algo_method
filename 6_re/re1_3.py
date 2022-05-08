# -*- coding: utf-8 -*-
import re
if __name__ == "__main__":
    input_str = input()
    ans_str = "No"
    reg_str = r"^a{1, 5}b{10}c*$"
    searched_result = re.search(reg_str, input_str)
    if searched_result:
        ans_str = "Yes"
    print(ans_str)
