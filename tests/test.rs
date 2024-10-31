use analyze::*;
// use polars::prelude::*;

#[test]
fn test_read_csv() -> Result<(), Box<dyn std::error::Error>> {
    let df = read_csv("data/bad-drivers.csv")?;
    assert_eq!(df.width(), 8);
    Ok(())
}