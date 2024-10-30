install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --ignore-patterns=test_.*?py *.py

test:
	python -m pytest -cov=analyze/src test_*.py

all:
	install format lint test