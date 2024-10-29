from analyze import descriptive_stats

def test_descriptive_stats():
    df = descriptive_stats()
    assert df.shape == (8,7)
    return