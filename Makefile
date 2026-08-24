install:
	pip install -r requirements.txt

run:
	python app.py

test:
	pytest -q

format:
	black app.py src tests
