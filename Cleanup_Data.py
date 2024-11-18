import os
import re

# 1st file
# change foler path, word_to_remove, and line_to_remove as needed

def process_files(folder_path, word_to_remove, line_to_remove):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    page_pattern = re.compile(r'^page\s+\d+$', re.IGNORECASE)

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                processed_lines = []
                for line in lines:
                    line = line.strip()
                    if line_to_remove not in line and not page_pattern.match(line):
                        line = line.replace(word_to_remove, '')
                        if line:
                            processed_lines.append(line + '\n')

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(processed_lines)
                
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

folder_path = r'/path/to/folder/of/txt/file(s)' 
word_to_remove = 'trash_word'
line_to_remove = 'word_in_trash_line'

process_files(folder_path, word_to_remove, line_to_remove)
print("Processing complete.")