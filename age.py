
from datetime import date, timedelta, datetime


#then subtracting one if the current month/day precedes the birth month/day.

def past_date(past_date, cur_date=date.today()):
    age = cur_date.year - past_date.year
    if cur_date.strftime('%d/%m') < past_date.strftime('%d/%m'):
        age -= 1
    return age


def future_date(future_date, cur_date=date.today()):
    return cur_date.year - future_date.year

def calculate_years(user_date, cur_date=date.today()):
    if user_date < cur_date:
        return past_date(user_date)
    else:
        return future_date(user_date)

def get_user_date():
    user_date = input("Please enter a date in the format of dd/mm/yyyy: ")
    datetim = datetime.strptime(user_date, '%d/%m/%Y')
    return datetim.date()


def main():
    user_date = get_user_date()
    print("You are: {}".format(calculate_years(user_date)))


if __name__ == "__main__":
    main()
