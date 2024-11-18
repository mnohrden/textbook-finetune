import csv
import json

# 4th file
# This file converts a CSV file to Alpaca JSON format which can be used by Unsloth for finetuning
# change the path to your CSV and JSON file

def csv_to_alpaca_json(csv_file, json_file):
    alpaca_data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:

            if len(row) < 2:
                continue 

            question = row[0].strip()
            answer = row[1].strip()
            alpaca_entry = {
                "instruction": question,
                "input": "",  
                "output": answer
            }
            alpaca_data.append(alpaca_entry)

    with open(json_file, mode='w', encoding='utf-8') as json_file:
        json.dump(alpaca_data, json_file, ensure_ascii=False, indent=4)

# change as needed
csv_file_path = '/path/to/csv_file.csv'
json_file_path = '/path/to/output.json'

csv_to_alpaca_json(csv_file_path, json_file_path)

print(f"Converted {csv_file_path} to {json_file_path} in Alpaca JSON format.")
