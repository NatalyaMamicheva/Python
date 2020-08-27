import json
with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    review = []
    for lines in f_obj:
        if "\n" in lines:
            review.append(lines[:-1].split())
        else:
            review.append(lines.split())

review_2 = []
l = []
for i in range(len(review)):
    review_2.append([review[i][0], (int(review[i][2]) - int(review[i][3]))])
    if (int(review[i][2]) - int(review[i][3])) >= 0:
        l.append((int(review[i][2]) - int(review[i][3])))

firm = {review[i][0] : (int(review[i][2]) - int(review[i][3])) for i in range(len(review))}

firm_2 = {"average_profit": (sum(l) / len(l))}

company = [firm, firm_2]

with open("text_7.json", "w", encoding="utf-8") as f_obj:
    json.dump(company, f_obj)