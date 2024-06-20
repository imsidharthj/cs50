import sys
import re
from datetime import date, datetime, timedelta
import inflect
p = inflect.engine()
def main():
    birth_date_str = input("date in format YYYY-MM-DD: ")
    try:
        year, month, day = check_date(birth_date_str)
    except:
        sys.exit("Invalid date")
    birth_date = date(year, month, day)
    current_date = date.today()
    # p_year, p_month, p_day, = check_date("2000-01-01")
    # current_date = date(p_year, p_month, p_day)
    days_diff = (current_date - birth_date).days
    age_minutes = days_diff * 24 * 60
    age_minutes_without_and = p.number_to_words(age_minutes, andword="").capitalize()
    print(f"{age_minutes_without_and} minutes")

def check_date(date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date):
        year, month, day = date.split("-")
        return int(year), int(month), int(day)

if __name__ == "__main__":
    main()