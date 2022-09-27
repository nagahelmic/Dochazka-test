import calendar
import datetime


# Vrátí počet dnů v měsíci
def pocet(mesic):
    mesic_pocet_dnu = calendar.monthrange(2022, mesic)
    return mesic_pocet_dnu[1]


def datumy(mesic, den):
    dates_in_month = []
    for day in range(1, pocet(mesic) + 1):
        date = datetime.date(2022, mesic, day)
        str_date = f"{date.day}.{date.month}.{date.year}"
        dates_in_month.append(str_date)
    return dates_in_month[den]
