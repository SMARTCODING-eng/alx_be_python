from datetime import date, datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# display_current_datetime()
def calculate_future_date():
    User_date = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta(days=User_date)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date()