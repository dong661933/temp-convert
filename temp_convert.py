"""A tiny command-line temperature converter.

Usage:
    python temp_convert.py <value> <c2f|f2c>

Examples:
    python temp_convert.py 100 c2f   ->  100.0 C = 212.0 F
    python temp_convert.py 32 f2c    ->  32.0 F = 0.0 C
"""
import sys


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main(argv):
    """Parse command-line arguments and print the converted temperature."""
    if len(argv) != 2:
        print("Usage: python temp_convert.py <value> <c2f|f2c>")
        return 1

    try:
        value = float(argv[0])
    except ValueError:
        print(f"Not a number: {argv[0]!r}")
        return 1

    direction = argv[1].lower()
    if direction == "c2f":
        print(f"{value} C = {round(celsius_to_fahrenheit(value), 2)} F")
    elif direction == "f2c":
        print(f"{value} F = {round(fahrenheit_to_celsius(value), 2)} C")
    else:
        print(f"Unknown direction: {direction!r} (use c2f or f2c)")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
