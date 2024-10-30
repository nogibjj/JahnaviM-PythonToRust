'''This file defaults to reading a dataset about bad drivers.
It produces summary statistics'''

import polars as pl
from datetime import datetime
import resource

def calculate_mean(csv_file="data/bad-drivers.csv", column_name="ins_loss"):
    '''Finds the mean of <column_name> in the csv_file'''
    df = pl.read_csv(csv_file)
    mean = df[column_name].mean()
    return mean

if __name__ == "__main__":
    
    start_time = datetime.now()
    start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    mean = calculate_mean()

    duration = datetime.now() - start_time

    stop_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    memory_used = stop_memory - start_memory

    print("")
    print("------------------------- PYTHON DIAGNOSTICS -------------------------")
    print(f"Average insurance loss for fatal car accidents: {mean}")
    print(f"Duration of this process in Rust: {duration}")
    print(f"Memory used by this process in Rust: {memory_used} kB")
    print("----------------------------------------------------------------------")
    print("")
