install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --ignore-patterns=test_.*?py *.py

test:
	python -m pytest -cov=crime_analyze test_crime_analyze.py

all:
	install format lint test