from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def local_add_demo() -> tuple[datetime, datetime]:
    utc = ZoneInfo("UTC")
    central = ZoneInfo("America/Chicago")

    local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
    wrong = local_dt + timedelta(minutes=30)

    utc_dt = local_dt.astimezone(utc)
    correct = (utc_dt + timedelta(minutes=30)).astimezone(central)
    return wrong, correct


def convert_input_to_utc(user_input: str) -> tuple[datetime, datetime]:
    utc = ZoneInfo("UTC")
    central = ZoneInfo("America/Chicago")
    taipei = ZoneInfo("Asia/Taipei")

    naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
    stored_utc = naive.replace(tzinfo=central).astimezone(utc)
    return stored_utc, stored_utc.astimezone(taipei)


def main() -> None:
    wrong, correct = local_add_demo()
    print(f"direct local add: {wrong}")
    print(f"utc-first add: {correct}")

    stored_utc, taipei_view = convert_input_to_utc("2012-12-21 09:30:00")
    print(f"store as UTC: {stored_utc}")
    print(f"display in Taipei: {taipei_view}")


if __name__ == "__main__":
    main()
