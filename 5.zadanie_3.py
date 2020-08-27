with open("text_3.txt", 'r', encoding="utf-8") as f_obj:
    salary = []
    job = []
    lines = f_obj.readlines()
    for i in lines:
        i = i.split()
        if float(i[1]) < 20000:
            job.append(i[0])
        salary.append(i[1])
print(f"Оклад меньше 20000 у сотрудников: {', '.join(job)}.\nСредняя величина дохода сотрудников: {sum(map(float, salary)) / len(salary)}")