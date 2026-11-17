# Deadline Date Formatter - Version 2.0 (Added weekday input and output)
import datetime


def main():
    event_title = input("Enter the event title: ")
    year = input("Enter the year (YYYY): ")
    month = input("Enter the month (MM): ")
    day = input("Enter the day (DD): ")

    event_upper = event_title.upper()

    event_date = datetime.date(int(year), int(month), int(day))
    readable_date = event_date.strftime("%B %d, %Y")
    month_name = event_date.strftime("%B")
    weekday_name = event_date.strftime("%A")

    print("\nEvent Information:")
    print(f"Event: {event_upper}")
    print(f"Date: {readable_date}")
    print(f"Year: {year}")
    print(f"Month: {month_name}")
    print(f"Day: {day}")
    print(f"Weekday: {weekday_name}")

if __name__ == "__main__":
    main()