"""Provide small, explicit math tools without evaluating arbitrary code."""

from __future__ import annotations

import math
from decimal import Decimal, InvalidOperation
from statistics import mean, median
from typing import Literal

from mcp.server import MCPServer


mcp = MCPServer("coding-lounge-math")


def _number(value: float) -> Decimal:
    if not math.isfinite(value):
        raise ValueError("Numbers must be finite.")
    return Decimal(str(value))


@mcp.tool()
def calculate(
    left: float,
    operation: Literal["add", "subtract", "multiply", "divide", "power"],
    right: float,
) -> str:
    """Calculate using one explicit operation; arbitrary code is never evaluated."""
    first = _number(left)
    second = _number(right)

    if operation == "add":
        result = first + second
    elif operation == "subtract":
        result = first - second
    elif operation == "multiply":
        result = first * second
    elif operation == "divide":
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        result = first / second
    else:
        if not right.is_integer() or abs(right) > 100:
            raise ValueError("Powers require a whole-number exponent from -100 to 100.")
        try:
            result = first ** int(right)
        except InvalidOperation as error:
            raise ValueError("That power is not a real finite number.") from error

    return format(result.normalize(), "f")


@mcp.tool()
def convert_temperature(
    value: float,
    from_unit: Literal["celsius", "fahrenheit", "kelvin"],
    to_unit: Literal["celsius", "fahrenheit", "kelvin"],
) -> float:
    """Convert a temperature between Celsius, Fahrenheit, and Kelvin."""
    if not math.isfinite(value):
        raise ValueError("Temperature must be finite.")

    celsius = {
        "celsius": value,
        "fahrenheit": (value - 32) * 5 / 9,
        "kelvin": value - 273.15,
    }[from_unit]
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero.")

    return {
        "celsius": celsius,
        "fahrenheit": celsius * 9 / 5 + 32,
        "kelvin": celsius + 273.15,
    }[to_unit]


@mcp.tool()
def calculate_percentage(part: float, whole: float) -> float:
    """Calculate what percentage one finite number is of another."""
    part_number = _number(part)
    whole_number = _number(whole)
    if whole_number == 0:
        raise ValueError("The whole value cannot be zero.")
    return float(part_number / whole_number * 100)


@mcp.tool()
def summarize_numbers(values: list[float]) -> dict[str, float | int]:
    """Return count, minimum, maximum, mean, and median for finite numbers."""
    if not values:
        raise ValueError("Provide at least one number.")
    if len(values) > 1_000:
        raise ValueError("Provide no more than 1,000 numbers.")
    if any(not math.isfinite(value) for value in values):
        raise ValueError("Numbers must be finite.")

    return {
        "count": len(values),
        "minimum": min(values),
        "maximum": max(values),
        "mean": mean(values),
        "median": median(values),
    }


if __name__ == "__main__":
    mcp.run()