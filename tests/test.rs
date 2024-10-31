use analyze::*;
// use polars::prelude::*;

#[test]
fn test_read_csv() -> Result<(), Box<dyn std::error::Error>> {
    let df = read_csv("data/bad-drivers.csv")?;
    assert_eq!(df.width(), 8);
    Ok(())
}

// #[test]
// fn test_calculate_mean() -> Result<(), Box<dyn std::error::Error>> {
//     let df = read_csv("data/bad-drivers.csv")?;
//     let mean = calculate_mean(&df, "ins_loss")?.unwrap_or(0.0);
//     assert_eq!(mean as i64, 134);
//     Ok(())
// }