/*
Basic Rust script that performs data processing on bad driver data.
*/

use polars::prelude::*;
use std::error::Error;
use std::time::Instant;
use sysinfo::System;

fn read_csv(filename: &str) -> Result<DataFrame, PolarsError> {
    let df = CsvReader::from_path(filename)?
        .has_header(true)
        .finish()?;
    Ok(df)
}

fn calculate_mean(df: &DataFrame, column_name: &str) -> Result<Option<f64>, PolarsError> {
    let series = df.column(column_name)?;
    let mean = series.f64()?.mean();  
    
    Ok(mean)
}

fn main() -> Result<(), Box<dyn Error>> {
    // initialize trackers for time and memory used
    let start_time = Instant::now();

    let system = System::new_all();
    let start_memory = system.used_memory();

    // triger data processing
    let df = read_csv("data/bad-drivers.csv")?;
    let mean = calculate_mean(&df, "ins_loss")?.unwrap_or(0.0);

    // measure duration and memory used
    let stop_time = start_time.elapsed();

    let stop_memory = system.used_memory();
    let memory_used = stop_memory - start_memory;

    // output summary statistics
    println!("");
    println!("------------------------- RUST DIAGNOSTICS -------------------------");
    println!("Average insurance loss for fatal car accidents: {:?}", mean);
    println!("Duration of this process in Rust: {:?}", stop_time);
    println!("Memory used by this process in Rust: {:?} kB", memory_used);
    println!("--------------------------------------------------------------------");
    println!("");

    Ok(())
}
