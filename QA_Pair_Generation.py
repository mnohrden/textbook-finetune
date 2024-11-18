import os
import nltk
import csv
import asyncio
from nltk.tokenize import word_tokenize
import ollama
import aiofiles
import time
from tqdm import tqdm 

# 2nd file
# This file generates input-output pairs from the folder of cleaned-up text files
# Please read each section with ------- around it carefully to change the parameters as needed

nltk.download('punkt')
nltk.download('punkt_tab')

# Folder containing the .txt files
folder_path = r'/path/to/folder/of/txt/file(s)'
# CSV file to save input-output pairs
csv_file_path = r'/path/to/output.csv'

   
#-------------------------------------------------
# Change to the Ollama model you want to use: https://ollama.com/search
# Note: Use the best model possible, you want high-quality data so use a smart model even if it takes a while.
# I have an RTX3060 12GB. I found that phi3:medium-128k was the smallest model that would give acceptable results.

# If you can run this in the cloud, you probably should, especially if your GPU doesn't have much VRAM
model = "phi3:medium-128k"
#-------------------------------------------------


#-------------------------------------------------
# Change to short description of the topic of interest
context = "thermodynamics"
#-------------------------------------------------


#-------------------------------------------------
# You will definitely want to change this part of the prompt. This is an example, but use it as a guideline
sample_qa_pair = (
    "Question: In the context of thermodynamics, consider a room whose door and windows are tightly closed, "
    "and whose walls are well-insulated so that heat loss or gain through the walls is negligible. "
    "Now let’s place a refrigerator in the middle of the room with its door open, and plug it into a wall outlet. "
    "Now, what do you think will happen to the average temperature of air in the room?\n"
    "Answer: If we take the entire room as the system, which is an adiabatic closed system since the room is well-sealed and well-insulated, "
    "the only energy interaction involved is the electrical energy crossing the system boundary and entering the room. "
    "Therefore, this energy must now be in the room air, and it will manifest itself as a rise in the air temperature."
)
#-------------------------------------------------


request_for_qa = (
    "Provide a single question and answer pair based on the text above. "
    "The questions must begin with 'In the context of ...'. The answers should borrow, verbatim, from the text above. "
    "In providing each question, consider that the reader does not see or have access to any of the other questions for context. "
    "Vary the style and format of questions. Respond in plain text on a new line for each question and answer. "
    "Do not include question numbers. Here is an example of the new question answer pair\n\n"
)

static_prompt = "context: " + context + "\n" + request_for_qa + sample_qa_pair

def split_into_chunks(text, chunk_size):
    tokens = word_tokenize(text)
    chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]
    return chunks

async def async_generate_ollama(chunk, model, prompt_template):
    input_chunk = ' '.join(chunk)
    prompt = input_chunk + prompt_template

    try:
        response = await asyncio.to_thread(ollama.generate, model, prompt)
        return input_chunk, response['response']
    except Exception as e:
        print(f"Error generating response for chunk: {e}")
        return input_chunk, "Error generating response"

def extract_question_answer(response):
    question = ""
    answer = ""
    
    if "Question:" in response and "Answer:" in response:
        try:
            question_part = response.split("Question:")[1]
            answer_part = question_part.split("Answer:")
            question = answer_part[0].strip()
            answer = answer_part[1].strip()
        except IndexError:
            print("Error splitting question and answer.")
    
    return question, answer

async def main():
    start_time = time.time()
    async with aiofiles.open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        await csvwriter.writerow(['Question', 'Answer'])

        txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        
        for filename in tqdm(txt_files, desc="Processing files"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            #---------------------------------------
            # Change based on how many tokens you want in each chunk fed to the model.
            # This depends on the context of the book you're using, but I found 200 be good for the textbook I was using
            chunk_size=200
            #---------------------------------------

            chunks = split_into_chunks(text, chunk_size)
            tasks = [async_generate_ollama(chunk, model, static_prompt) for chunk in chunks]
            results = await asyncio.gather(*tasks)

            for input_chunk, response in results:
                question, answer = extract_question_answer(response)
                await csvwriter.writerow([question, answer])
    elapsed_time = time.time() - start_time
    print(f"Completed in {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
