
from datetime import date, timedelta

def past_date(past_date, cur_date=date.today()):
    return cur_date.year - past_date.year


def future_date(future_date, cur_date=date.today()):
    return past_date.year - cur_date.year

def if_past(user_date, cur_date=date.today()):
    if user_date < cur_date:
        return True
    else:
        False


def main():
    user_date = date(2033, 12, 30)
    if if_past(user_date):
        print(past_date(user_date))
    else:
        print(future_date(user_date))


if __name__ == "__main__":
    main()
