# Finetune an LLM on Your Own Books!
Currnetly will fineune a 4bit quantized version of Llama3.1-8b, but you can change this to any model supported by unsloth: https://docs.unsloth.ai/get-started/all-our-models

Use the files in order and follow all the instructions:
1. Cleanup_Data.py
2. QA_Pair_Generation.py
3. Find_Max_Tokens_In_Cell_Of_CSV.py
4. Convert_CSV_To_Alpaca_Style_JSON .py <- OK honestly I made a private version of this repo a while ago and had this file in there but I don't know why you need this
5. Finetune_LLM_Using_Unsloth.py