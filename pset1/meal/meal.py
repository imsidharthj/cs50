def main():
   time = input("what time it is? ")
   timehours = convert(time)

   if 7 <= timehours < 8:
      print("breakfast time")
   elif 12 <= timehours <= 13:
      print("lunch time")
   elif 18 <= timehours < 19:
      print("dinner time")

def convert(time):
   hours, minutes = time.split(":")
   hours = float(hours)
   minutes = float(minutes)
   timehours = ((hours * 60) + minutes) / 60
   return timehours

if __name__ == "__main__":
   main()