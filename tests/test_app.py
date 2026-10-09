from app import calculate_one_rep_max


def test_one_rep_max():
    result = calculate_one_rep_max(225, 5)

    assert result == 262.5