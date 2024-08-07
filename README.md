# LLM Workshop 2024

> [!IMPORTANT]
> :dart: [DataHack Summit 2024](https://www.analyticsvidhya.com/datahacksummit/workshops/unleashing-llms-training-finetuning-and-evaluating) | :calendar: August 10 2024 | :round_pushpin: Bengaluru, India

> Explore this comprehensive repository on LLMs, covering everything from the basics of NLP to fine-tuning and even RLHF. If you find the resources helpful, consider giving it a star ⭐ to show your support and help others discover it.
---
## Table of Contents
- [Modules](#modules)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup-instructions)

---

### Modules
#### Module 1: "Foundations of Generative AI and Language Models"
- [x] Overview of Generative AI and the basics of language modeling.
- [x] :star: Hands-On: 
    - [x] Getting Started: Text Representation
    - [x] Language Modeling Basics and Text Generation using a basic LM.

#### Module 2: "Building Blocks of LLMs"
- [x] Transformer Architectures: Detailed look into the Transformer architecture that powers modern LLMs.
- [x] GPT Series of Models: Overview of the evolution of GPT models.
- [x] Evaluation Metrics and Benchmarks: Methods to evaluate and benchmark LLM performance.
- [x] :star: Hands-On: Training a mini Transformer model and experimenting with GPT-2 for text generation.

#### Module 3: "Advanced LLM Techniques"
- [x] Training Process and Scaling Laws: Understand how LLMs are trained and the laws governing their scaling.
- [x] PEFT: Learn Parameter-Efficient Fine-Tuning methods.
- [x] LoRA: Introduction to Low-Rank Adaptation.
- [x] Instruction Tuning: Techniques for fine-tuning models using instructions.
- [x] RLHF: Reinforcement Learning from Human Feedback and its applications.
- [x] :star: Hands-On:
    - [x] Instruction Tuning: Text 2 SQL using LLaMA3.1
    - [x] RLHF Hands-on: Sentiment aligment for generating movie reviews

#### Module 4: "Operationalizing LLMs"
- [x] Prompt Engineering: Crafting effective prompts to get desired outputs.
- [x] Prompt Hacking and Backdoors
- [x] Vector Databases: Using vector databases for efficient data retrieval.
- [x] RAGs: Techniques for retrieval-augmented generation.
- [x] Beyond Prompting: Understanding Frameworks such as DSPY
- [x] :star: Hands-On:
    - [x] Implementing basic prompt engineering techniques and
    - [x] Building a simple RAG system.
    - [x] Handson with DSPY

#### Module 5: "The Future of LLMs and Next Steps"
- Next Steps: Speculative topics on future advancements.
- Beyond: Future possibilities and directions for LLM research.

---

### Prerequisites
- Basics/hands-on experience of working with python
- Basic understanding of linear algebra and machine larning
- Basic understanding of Deep Neural Networks
- Basics/hands-on experience with pytorch
- Access to google-colab or similar python environment
- Access to chatGPT or Google-Bard (free access) 

---

## Environment Setup Instructions

> [!Important]
> - Follow Step by Step for a quick setup. This should work as-is for Mac/Linux based systems.
> - If you already have your own way of managing dependencies, checkout pyproject.toml for poetry or requirements.txt for pip based systems
> - The requirements.txt file is generated using the command ``poetry export --without-hashes --format=requirements.txt > requirements.txt``

- **We will make use of** :
    - ``pyenv`` for python version management
    - ``virtualenv`` for virtual environment management
    - ``poetry`` for dependency management

- **Pyenv**: 
    - ``brew install pyenv`` or ``curl https://pyenv.run | bash``
- **VirtualEnv**: 
    - install: 
        - ``brew install pyenv-virtualenv`` or
        - ``git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv``
    - add this to your .rc file: ``eval "$(pyenv virtualenv-init -)"``
- **Poetry**:
    - install: 
        - ``curl -sSL https://install.python-poetry.org | python3 -`` or
        - or check [here](https://python-poetry.org/docs/#installing-with-the-official-installer)

- **Setup**:
    - Local Mac/Linux :If you have `make` available, simply execute: ``make setup`` otherwise:
    - RunPod or other Similar Providers: simply execute: ``make runpod_setup`` otherwise:
    - If you are using other ways of dependency management:
        - Python Environment:
            -``pyenv install 3.11.9``
            - ``pyenv virtualenv 3.11.9 datahack``
            - ``cd <path to this repo clone>``
            - ``pyenv activate datahack``
            - ``poetry install`` <- Make sure ``pyproject.toml`` file is available in directory you execute this command
            OR
            - use the `requirements.txt` file for reference.
        - Setup ``nvm`` / ``node`` and install ``localtunnel``
    



