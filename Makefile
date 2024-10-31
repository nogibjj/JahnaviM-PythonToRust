rust-version:
	@echo "Rust command-line utility versions:"
	rustc --version 			#rust compiler
	cargo --version 			#rust package manager
	rustfmt --version			#rust code formatter
	rustup --version			#rust toolchain manager
	clippy-driver --version		#rust linter

rs_format:
	cargo fmt --quiet

rs_install:
	cargo install --path .

rs_lint:
	cargo clippy --quiet

rs_test:
	cargo test --quiet

rs_run:
	cargo run

rs_release:
	cargo build --release

py_install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

py_test:
	python -m pytest -vv --cov=src tests/test_*.py

py_format:	
	black src/*.py 

py_lint:
	ruff check src/*.py test/test_*.py

py_refactor: format lint
