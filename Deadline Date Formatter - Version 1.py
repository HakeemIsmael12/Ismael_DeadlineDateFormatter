# Deadline Date Formatter - Version 1.0 (Initial version - basic input and output)
def main():
    event_title = input("Enter the event title: ")
    year = input("Enter the year (YYYY): ")
    month = input("Enter the month (MM): ")
    day = input("Enter the day (DD): ")

    print("\nEvent Information:")
    print(f"Event Title: {event_title}")
    print(f"Date: {year}{month}, {day}")
    print(f"Year: {year}")
    print(f"Month: {month}")
    print(f"Day: {day}")
    print(f"Weekday: Not Specified")


if __name__ == "__main__":
    main()
