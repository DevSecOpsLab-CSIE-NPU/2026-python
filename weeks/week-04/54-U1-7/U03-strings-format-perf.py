import timeit


PARTS = [f"item{i}" for i in range(1000)]


def bad_concat() -> str:
    result = ""
    for part in PARTS:
        result += part
    return result


def good_join() -> str:
    return "".join(PARTS)


class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def main() -> None:
    concat_time = timeit.timeit(bad_concat, number=500)
    join_time = timeit.timeit(good_join, number=500)
    print(f"plus concat: {concat_time:.3f}s  join: {join_time:.3f}s")

    name = "Guido"
    template = "{name} has {n} messages."
    print(template.format_map(SafeSub(vars())))

    text_value = "Hello"
    byte_value = b"Hello"
    print(text_value[0])
    print(byte_value[0])

    formatted = "{:10s} {:5d}".format("ACME", 100)
    print(formatted.encode("ascii"))


if __name__ == "__main__":
    main()
