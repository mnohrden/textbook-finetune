# Finetune an LLM on Your Own Textbooks!
Currnetly will fineune a 4bit quantized version of Llama3.1-8b, but you can change this to any model supported by unsloth: https://docs.unsloth.ai/get-started/all-our-models

Unsloth has dependencies that only work on Linux so use WSL if you're on Windows.

Install Ollama:
```
curl -fsSL https://ollama.com/install.sh | sh
```
Find a model you want for generating Q/A pairs: https://ollama.com/search.
See QA_Pair_Generation.py for advice on choosing a model, or if you should just run this file in the cloud.
```
ollama run phi3:medium-128k
```
Install Unsloth:
https://github.com/unslothai/unsloth?tab=readme-ov-file#-installation-instructions

Install PyTorch
https://pytorch.org/get-started/locally/

Install Python Packages, this _should_ be all the ones you need
```
pip install nltk asyncio ollama aiofiles tqdm
```

Now that you did all that you can use the files in order and follow all the instructions:

1. Cleanup_Data.py
2. QA_Pair_Generation.py
3. Find_Max_Tokens_In_Cell_Of_CSV.py
4. Convert_CSV_To_Alpaca_Style_JSON .py
5. Finetune_LLM_Using_Unsloth.py

I hope you find this useful/interesting!
