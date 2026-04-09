import re
import timeit
from calendar import month_abbr

TEXT = "Today is 11/27/2012. PyCon starts 3/13/2013."
DATE_PATTERN = re.compile(r"(\d+)/(\d+)/(\d+)")


def find_dates_module() -> list[tuple[str, str, str]]:
    return re.findall(r"(\d+)/(\d+)/(\d+)", TEXT)


def find_dates_compiled() -> list[tuple[str, str, str]]:
    return DATE_PATTERN.findall(TEXT)


def convert_to_named_month(match: re.Match[str]) -> str:
    month_name = month_abbr[int(match.group(1))]
    return f"{match.group(2)} {month_name} {match.group(3)}"


def match_case(word: str):
    def replace(match: re.Match[str]) -> str:
        token = match.group()
        if token.isupper():
            return word.upper()
        if token.islower():
            return word.lower()
        if token[0].isupper():
            return word.capitalize()
        return word

    return replace


def main() -> None:
    module_time = timeit.timeit(find_dates_module, number=50_000)
    compiled_time = timeit.timeit(find_dates_compiled, number=50_000)
    print(f"module: {module_time:.3f}s, compiled: {compiled_time:.3f}s")

    print(DATE_PATTERN.sub(convert_to_named_month, TEXT))

    sample = "UPPER PYTHON, lower python, Mixed Python"
    print(re.sub("python", match_case("snake"), sample, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()
