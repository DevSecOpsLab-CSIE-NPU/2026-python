import calendar
import timeit
from datetime import datetime, timedelta

def add_one_month(value: datetime) -> datetime:
    year = value.year
    month = value.month + 1
    if month == 13:
        year += 1
        month = 1

    _, max_day = calendar.monthrange(year, month)
    day = min(value.day, max_day)
    return value.replace(year=year, month=month, day=day)


DATES = [f"2012-{month:02d}-{day:02d}" for month in range(1, 13) for day in range(1, 29)]


def use_strptime(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")


def use_manual(value: str) -> datetime:
    year, month, day = value.split("-")
    return datetime(int(year), int(month), int(day))


def main() -> None:
    current = datetime(2012, 9, 23)
    try:
        current + timedelta(months=1)
    except TypeError as error:
        print(f"TypeError: {error}")

    print(add_one_month(datetime(2012, 1, 31)))
    print(add_one_month(datetime(2012, 9, 23)))

    assert use_strptime("2012-09-20") == use_manual("2012-09-20")

    strptime_time = timeit.timeit(lambda: [use_strptime(date) for date in DATES], number=100)
    manual_time = timeit.timeit(lambda: [use_manual(date) for date in DATES], number=100)
    print(f"strptime: {strptime_time:.3f}s  manual parse: {manual_time:.3f}s")


if __name__ == "__main__":
    main()
