rust-version:
	@echo "Rust command-line utility versions:"
	rustc --version 			#rust compiler
	cargo --version 			#rust package manager
	rustfmt --version			#rust code formatter
	rustup --version			#rust toolchain manager
	clippy-driver --version		#rust linter

format:
	cargo fmt --quiet

install:
	cargo install --path .

lint:
	cargo clippy --quiet

test:
	cargo test --quiet

run:
	cargo run

release:
	cargo build --release

python_install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

python_test:
	python -m pytest -vv --cov=src src/test_*.py

python_format:	
	black src/*.py 

python_lint:
	ruff check src/*.py src/test_*.py

python_refactor: format lint
