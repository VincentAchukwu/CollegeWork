import sys
import calendar

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

days_of_week = ["Monday's child is fair of face", "Tuesday's child is full of grace", "Wednesday's child is full of woe", "Thursday's child has far to go", "Friday's child is loving and giving", "Saturday's child works hard for a living", "Sunday's child is fair and wise and good in every way"]

def main():
    day = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])
    for i in range(0, 7):
        if calendar.weekday(year, month, day) == i:
            print("You were born on a {} and {}.".format(days[i], days_of_week[i]))

if __name__ == '__main__':
     main()
