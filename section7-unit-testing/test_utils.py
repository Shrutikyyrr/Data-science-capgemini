"""
Section 7: Unit tests for utility functions (utils.py)
Tests pure functions — no HTTP, no DB.
"""
import pytest
from utils import calculate_pass_probability, get_grade, is_valid_age


# ── calculate_pass_probability ────────────────────────────────────────────────

def test_probability_basic():
    assert calculate_pass_probability(30, 100) == 0.3


def test_probability_all_pass():
    assert calculate_pass_probability(100, 100) == 1.0


def test_probability_none_pass():
    assert calculate_pass_probability(0, 100) == 0.0


def test_probability_zero_total_raises():
    with pytest.raises(ValueError, match="Total must be greater than 0"):
        calculate_pass_probability(10, 0)


def test_probability_negative_total_raises():
    with pytest.raises(ValueError):
        calculate_pass_probability(10, -5)


def test_probability_passed_exceeds_total_raises():
    with pytest.raises(ValueError):
        calculate_pass_probability(110, 100)


# ── get_grade ─────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("score,expected", [
    (95, "A"),
    (90, "A"),
    (89, "B"),
    (75, "B"),
    (74, "C"),
    (60, "C"),
    (59, "D"),
    (50, "D"),
    (49, "F"),
    (0,  "F"),
])
def test_get_grade_parametrized(score, expected):
    assert get_grade(score) == expected


# ── is_valid_age ──────────────────────────────────────────────────────────────

def test_valid_age_normal():
    assert is_valid_age(21) is True


def test_valid_age_min_boundary():
    assert is_valid_age(1) is True


def test_valid_age_max_boundary():
    assert is_valid_age(100) is True


def test_invalid_age_zero():
    assert is_valid_age(0) is False


def test_invalid_age_negative():
    assert is_valid_age(-5) is False


def test_invalid_age_over_max():
    assert is_valid_age(101) is False
