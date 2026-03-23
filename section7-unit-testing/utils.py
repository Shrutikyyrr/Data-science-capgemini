"""Utility functions — tested independently in test_utils.py"""


def calculate_pass_probability(passed: int, total: int) -> float:
    """Return probability of passing as float 0–1."""
    if total <= 0:
        raise ValueError("Total must be greater than 0")
    if passed < 0 or passed > total:
        raise ValueError("passed must be between 0 and total")
    return round(passed / total, 4)


def get_grade(score: float) -> str:
    """Return letter grade A–F based on score."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def is_valid_age(age: int) -> bool:
    """Check if age is in valid student range (1–100)."""
    return 1 <= age <= 100
