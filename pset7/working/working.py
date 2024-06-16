import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^([1-9]|1[0-2]):*([0-5][0-9])* (AM|PM) to ([1-9]|1[0-2]):*([0-5][0-9])* (AM|PM)$", s, re.IGNORECASE)
    if match:
        start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
        
        start_minute = start_minute or '00'
        end_minute = end_minute or '00'

        start_hour = int(start_hour)
        end_hour = int(end_hour)
        start_minute = int(start_minute)
        end_minute = int(end_minute)

        if not (0 <= start_hour <= 12) or not (0 <= end_hour <= 12):
            raise ValueError
        elif not (0 <= start_minute <= 59) or not (0 <= end_minute <= 59):
            raise ValueError

        start_24 = convert_time(start_hour, start_minute, start_period)
        end_24 = convert_time(end_hour, end_minute, end_period)
        
        return f"{start_24} to {end_24}"
    else:
        raise ValueError

def convert_time(hour, minute, period):
    if period.upper() == "PM" and hour != 12:
        hour += 12
    elif period.upper() == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
# import re
# import sys

# def main():
#     print(convert(input("Hours: ")))

# def convert(s):
#     # Modified regex to make " to " mandatory
#     match = re.search(r"^([1-9]|1[0-2]):*([0-5][0-9])* (AM|PM) to ([1-9]|1[0-2]):*([0-5][0-9])* (AM|PM)$", s, re.IGNORECASE)
#     if match:
#         start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
        
#         start_minute = start_minute or '00'
#         end_minute = end_minute or '00'

#         start_hour = int(start_hour)
#         end_hour = int(end_hour)
#         start_minute = int(start_minute)
#         end_minute = int(end_minute)

#         if not (0 <= start_hour <= 12) or not (0 <= end_hour <= 12):
#             raise ValueError
#         elif not (0 <= start_minute <= 59) or not (0 <= end_minute <= 59):
#             raise ValueError

#         start_24 = convert_time(start_hour, start_minute, start_period)
#         end_24 = convert_time(end_hour, end_minute, end_period)
        
#         return f"{start_24} to {end_24}"
#     else:
#         raise ValueError

# def convert_time(hour, minute, period):
#     if period.upper() == "PM" and hour != 12:
#         hour += 12
#     elif period.upper() == "AM" and hour == 12:
#         hour = 0

#     return f"{hour:02}:{minute:02}"

# if __name__ == "__main__":
#     main()
