# Jahnavi Maddhuri: Python to Rust
In this project I create a build system for both python and rust scripts. My scripts are identical in nature and both use polars to find the average insurance loss of the same dataset. I create these scripts to compare the proficiencies of both language in terms of duration and storage. This system creates a base feedback loop every time I update my project.

## CI/CD Badge
[![CICD - Python](https://github.com/nogibjj/JahnaviM-PythonToRust/actions/workflows/cicd_python.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-PythonToRust/actions/workflows/cicd_python.yml)
[![CICD - Rust](https://github.com/nogibjj/JahnaviM-PythonToRust/actions/workflows/cicd_rust.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-PythonToRust/actions/workflows/cicd_rust.yml)

## Instructions for Use
To use this repository to generate the analysis follow the steps below:
1. Start by cloning the repository. 
2. Make sure all the requirements in requirements.txt are fulfilled as these are necessary libraries to run the python script. Run `pip install -r requirements.txt`
3. Setup the rust script by navigating to src and running `cargo build --release`
4. Run the rust script by then running `cargo run`
5. Run the python script by running `python main.py`

## Sample Script Outputs
<img width="888" alt="image" src="https://github.com/user-attachments/assets/9419e972-ff9c-43b3-b81d-3841838e240b">


Both scripts in rust and python reported the same average loss in insurance. The rust script performed slightly faster by almost 25% and also consumed no memory while the python script used 17268736 kB. In this case, rust outperformed python.
