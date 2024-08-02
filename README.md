# LLM Workshop 2024

> [!IMPORTANT]
> :dart: [DataHack Summit 2024](https://www.analyticsvidhya.com/datahacksummit/workshops/unleashing-llms-training-finetuning-and-evaluating) | :calendar: August 10 2024 | :round_pushpin: Bengaluru, India

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
- [ ] Prompt Engineering: Crafting effective prompts to get desired outputs.
- [ ] RAGs: Techniques for retrieval-augmented generation.
- [ ] Vector Databases: Using vector databases for efficient data retrieval.
- [ ] Chunking and Ingesting Documents: Methods for processing and ingesting documents.
- [ ] Beyond Prompting: Understanding Frameworks such as DSPY
- [ ] Securing LLMs
- [ ] Prompt Hacking and Backdoors
- [ ] Defensive Measures
- [ ] :star: Hands-On:
    - [ ] Implementing basic prompt engineering techniques and
    - [ ] Building a simple RAG system.
    - [ ] Handson with DSPY

#### Module 5: "The Future of LLMs and Next Steps"
- Multi-modal: Integration of different data modalities in LLMs.
- Mixture of Experts: Using a mixture of expert models for improved performance.
- SLM: Introduction to Small LMs.
- Ethics and Bias in LLMs: Understanding and mitigating biases in LLMs.
- Next Steps: Speculative topics on future advancements.
- GPT5?: What to expect from the next generation of GPT.
- Beyond: Future possibilities and directions for LLM research.
-  :star: Hands-On: (If time permits) Experimenting with multi-modal models and mixture of experts.

---


> [!Note]
> Prerequisites
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
    - If you are on mac/linux and have `make` setup, simply execute: ``make setup`` otherwise:
    - ``pyenv install 3.11.9``
	- ``pyenv virtualenv 3.11.9 datahack``
    - ``cd <path to this repo clone>``
	- ``pyenv activate datahack``
	- ``poetry install`` <- Make sure ``pyproject.toml`` file is available in directory you execute this command
    - If you are using other ways of dependency management, use the `requirements.txt` file for reference.



