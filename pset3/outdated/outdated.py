def endian_iso(date_input, month_list):
        try:
            parts = date_input.split("/")
            if len(parts) == 3:
                month, day, year = parts
                day = int(day)
                if day > 31:
                    return None
                year = int(year)
                if month.isdigit():
                    month = int(month)
                    if month in range(1, 13):
                        return f"{year}-{month:02d}-{day:02d}"
                else:
                    return None

            else:
                parts = date_input.split(" ")
                if len(parts) == 3:
                    month = parts[0]
                    day = parts[1]
                    if day[-1] == ",":
                        day = day.strip(",")
                    else:
                        return None                      
                    year = parts[2]
                    day = int(day)
                    if day > 31:
                        return None
                    year = int(year)

                    if month in month_list:
                        month = month_list.index(month) + 1
                        return f"{year}-{month:02d}-{day:02d}"
                    else:
                        return None
                else:
                    return None
      
        except ValueError:
            return None

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
        date_input = input("Date: ").capitalize().strip()
        date_input = date_input.replace('"','')
        converted_date = endian_iso(date_input, month_list)
        if converted_date is not None:
            print(converted_date)
            break
        else:
            continue
main()