import re
with open('text_6.txt', 'r', encoding="utf-8") as f_obj:
    lines = f_obj.read()
    sstring = lines.split("\n")
    review = {}
    for item in sstring:
        key = item.split()[0]
        value = item.split()[1:]
        value_str = "".join(value)
        n_znach = re.sub("\D", " ", value_str)
        m_list = n_znach.split()
        result = [int(item) for item in m_list]
        review = {key: sum(result)}
        print(review, end=" ")