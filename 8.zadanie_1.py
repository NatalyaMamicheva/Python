class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def my_data(cls, day_month_year):
        dat = []

        for i in day_month_year.split():
            if i != "-":
                dat.append(i)

        print(f"{int(dat[0])} - {int(dat[1])} - {int(dat[2])}")

    @staticmethod
    def my_data_2(day, month, year):
        if (day > 0 and day < 32) and (month > 0 and month < 13) and (year > 0 and year < 2021):
            print(f"{day} - {month} - {year}, Данные введены верно")
        else:
            print(f"{day} - {month} - {year}, Данные введены неверно")

    def __str__(self):
        return f"Введенная дата: {self.day_month_year}"

d = Data("08 - 09 - 2020")
print(d)
Data.my_data("11 - 11 - 2011")
d.my_data("11 - 07 - 2008")
Data.my_data_2(11,9,2019)
d.my_data_2(0,11,2090)