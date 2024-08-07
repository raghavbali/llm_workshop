.PHONY: setup runpod_setup tests

setup:
	@echo "Setting up the environment..."
	pyenv install 3.11.9
	pyenv virtualenv 3.11.9 datahack
	pyenv activate datahack
	poetry install

runpod_setup:
	@echo "Setting up runpod environment..."
	@echo "Step 1 python dependencies..."
	pip install -r requirements.txt
	@echo "Step 2 nodes/npm dependencies..."
	wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
	nvm install node
	npm install localtunnel
	@echo "Step 2 ollama dependencies..."
	curl -fsSL https://ollama.com/install.sh | sh
	export OLLAMA_MODELS=/workspace
	ollama pull llama3.1:8b
	@echo "Done!"

tests:
	@echo "Running tests..."
	poetry run pytest --disable-warnings