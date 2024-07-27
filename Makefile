.PHONY: setup tests

setup:
	@echo "Setting up the environment..."
	pyenv install 3.11.9
	pyenv virtualenv 3.11.9 datahack
	pyenv activate datahack
	poetry install

tests:
	@echo "Running tests..."
	poetry run pytest --disable-warnings