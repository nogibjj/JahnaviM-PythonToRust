from crime_analyze import df

def test_df():
    assert df.shape == (974477, 29)
    return