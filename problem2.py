from datetime import datetime
from datetime import date


def convert_date(date_str, out):
    today = datetime.today()
    months = ['january', "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

    try:
        month = date_str[: date_str.find(" ")]
        if month.lower() in months:
            day = int(date_str[date_str.find(" ") + 1 : date_str.find(",")])
            year = int(date_str[date_str.find(", ") + 1:])

            current = datetime(year, months.index(month.lower()) + 1, day)
            if current <= today:
                out.write(current.strftime("%m/%d/%Y")+ "\n")
    except:
        return



inp = open('inputDates.txt', 'r')
out = open('parsedDates.txt', 'w')

for line in inp.readlines():
    if line == "-1":
        break
    convert_date(line.strip(), out)
out.close()
inp.close()
