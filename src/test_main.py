from main import calculate_mean

def test_calculate_mean():
    mean = calculate_mean('src/data/bad-drivers.csv')
    assert int(mean) == 134
    return