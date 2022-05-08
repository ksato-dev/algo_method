# -*- coding: utf-8 -*-
import re
if __name__ == "__main__":
    n, y, m = input().split()
    n = int(n)
    # reg_str = r"\d{8}.pdf"
    reg_str = r"^" + y + m.zfill(2) + r"\d{2}.pdf$"

    for n_id in range(n):
        pdf_str = input()
        split_str_list = pdf_str.split("_")
        title_str = split_str_list[1]
        postfix_str = split_str_list[2]

        if re.match(reg_str, postfix_str):
            print(title_str)
