#!/usr/bin/env python3
import sys


def parse_number(text: str) -> float:
    """Convert a string to a float, raising a clear error on failure."""
    try:
        return float(text)
    except ValueError as exc:
        raise ValueError(f"Invalid number: {text}") from exc


def add_three_numbers(a: float, b: float, c: float) -> float:
    """Return the sum of three numbers."""
    return a + b + c


def main() -> int:
    args = sys.argv[1:]

    numbers: list[float]
    if len(args) == 3:
        try:
            numbers = [parse_number(arg) for arg in args]
        except ValueError as error:
            print(error, file=sys.stderr)
            return 1
    else:
        numbers = []
        try:
            for index in range(3):
                value = input(f"Enter number {index + 1}: ").strip()
                numbers.append(parse_number(value))
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.", file=sys.stderr)
            return 1
        except ValueError as error:
            print(error, file=sys.stderr)
            return 1

    total = add_three_numbers(*numbers)
    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

