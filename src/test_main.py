from main import calculate_mean

def test_calculate_mean():
    mean = calculate_mean()
    assert int(mean) == 134
    return