import csv
import nltk
from nltk.tokenize import word_tokenize

# 3rd file
# this finds the maximum number of tokens in a cell of the CSV created.
# Make note of the result of this file as it will be used in the 5th file

def count_tokens_in_cell(cell):
    """Counts the number of tokens in a cell using NLTK's word_tokenize."""
    tokens = word_tokenize(cell)
    return len(tokens)

def find_max_tokens_in_csv(file_path):
    max_tokens = 0
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            for cell in row:
                tokens = count_tokens_in_cell(cell)
                if tokens > max_tokens:
                    max_tokens = tokens

    return max_tokens

# change as needed
csv_file_path = r"/path/to/your/csv/file.csv"

max_tokens = find_max_tokens_in_csv(csv_file_path)
print(f"The maximum number of tokens in any cell is: {max_tokens}")