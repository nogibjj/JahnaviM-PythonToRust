/*
Basic Rust script that performs data processing on bad driver data.
*/

use polars::prelude::*;
// use std::error::Error;
// use std::time::Instant;
// use sysinfo::System;

pub fn read_csv(filename: &str) -> Result<DataFrame, PolarsError> {
    let df = CsvReader::from_path(filename)?
        .has_header(true)
        .finish()?;
    Ok(df)
}

pub fn calculate_mean(df: &DataFrame, column_name: &str) -> Result<Option<f64>, PolarsError> {
    let series = df.column(column_name)?;
    let mean = series.f64()?.mean();  
    
    Ok(mean)
}
