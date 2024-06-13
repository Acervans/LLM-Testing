# LLM-Testing
Playground to test local Large Language Models with [ollama](https://ollama.com/), implementing functionalities such as function calling.

## Setup

1. Execute the following steps to install ollama's binaries and libraries, and create the models used in the playground.
   - __Note__: These steps correspond to Linux OS. For other OS, check [ollama](https://ollama.com/)'s webpage for installation instructions, then follow from __step B__.
```
# A. Install ollama (Linux)
curl -fsSL https://ollama.com/install.sh | sh

# B. Install required Python packages
pip install -r requirements.txt

# C. Run ollama server as a service
ollama serve

# D. Create models
ollama create weatherer --file weatherer/Modelfile  # Mistral 7B (4.1 GB disk, 5.8 GB memory)
```

2. List __installed models__ with `ollama ls`
   
3. List __mounted models__ with `ollama ps`

4. Check the notebooks containing each tested functionality.

## Uninstall

1. Remove all custom models with `ollama rm <Model Name>`

2. Follow ollama's instructions [here](https://github.com/ollama/ollama/blob/main/docs/linux.md#uninstall) (Linux).
