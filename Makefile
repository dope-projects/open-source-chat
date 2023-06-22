setup:
	pip install pre-commit
	pre-commit install
	python -m venv venv
	source venv/bin/activate

	pre-commit autoupdate

install:
	@ pip install --upgrade pip
	@ pip install -r requirements.txt

run:
	@python -m streamlit run app.py

install-tests:
	@ python -m pip install -r requirements-test.txt
 
test:
	@pytest -p no:cacheprovider
	@echo "testing complete"

clean:
	@echo "cleaning"
	@rm -rf __pycache__
	@rm -rf pytest_cache


.PHONY: run install clean setup test
