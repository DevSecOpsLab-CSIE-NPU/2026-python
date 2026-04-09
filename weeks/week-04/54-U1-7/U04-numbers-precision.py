import math
import timeit
from decimal import ROUND_HALF_UP, Decimal

def traditional_round(value: float, digits: int = 0) -> Decimal:
    decimal_value = Decimal(str(value))
    quant = Decimal("1") if digits == 0 else Decimal("0." + "0" * digits)
    return decimal_value.quantize(quant, rounding=ROUND_HALF_UP)


def main() -> None:
    print(round(0.5))
    print(round(2.5))
    print(round(3.5))

    print(traditional_round(0.5))
    print(traditional_round(2.5))

    nan_value = float("nan")
    print(nan_value == nan_value)
    print(nan_value == float("nan"))
    print(math.isnan(nan_value))

    data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
    filtered = [item for item in data if not math.isnan(item)]
    print(filtered)

    print(0.1 + 0.2)
    print(0.1 + 0.2 == 0.3)

    print(Decimal("0.1") + Decimal("0.2"))
    print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

    float_time = timeit.timeit(lambda: 0.1 * 999, number=100_000)
    decimal_time = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
    print(f"float: {float_time:.3f}s  Decimal: {decimal_time:.3f}s")


if __name__ == "__main__":
    main()
