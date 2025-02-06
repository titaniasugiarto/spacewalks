from eva_data_analysis import text_to_duration, calculate_crew_size
import pytest

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected value for durations
    with a non-zero minute component.
    """
    assert text_to_duration("10:20") == pytest.approx(10.3333333)

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected value for durations
    with typical whole hour durations
    """
    assert text_to_duration("10:00") == 10

@pytest.mark.parametrize("input_value, expected_result", [
    ("Owen Garriott;Jack Lousma;", 2),
    ("John Doe;", 1),
    ("Judith Resnik; Sally Ride;", 2)
])

def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns the expected crew size
    for a given list of crew members.
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

def test_calculate_crew_size_edge_case():
    assert calculate_crew_size("") is None