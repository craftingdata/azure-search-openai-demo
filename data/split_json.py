import json
import os
import sys

def split_json_file2(input_filepath):
    # Read the JSON file with UTF-8 encoding
    with open(input_filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(input_filepath), "split_pages")
    os.makedirs(output_dir, exist_ok=True)

    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(input_filepath))[0]

    # Create a new file for each entry in the JSON array
    for i, entry in enumerate(data):
        content = entry.get('content', '')
        if content is None:
            content = ''
        output_filepath = os.path.join(output_dir, f"{base_filename}_entry{i + 1}.md")
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            output_file.write(content)

    print(f"Created {len(data)} files from JSON entries successfully.")

def split_json_file(input_filepath, num_parts):
    # Read the JSON file with UTF-8 encoding
    with open(input_filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Calculate the number of entries per file
    num_entries = len(data)
    entries_per_file = num_entries // num_parts
    remainder = num_entries % num_parts

    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(input_filepath), "split_pages")
    os.makedirs(output_dir, exist_ok=True)

    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(input_filepath))[0]

    # Split the data and write to new JSON files
    start_index = 0
    for i in range(num_parts):
        end_index = start_index + entries_per_file + (1 if i < remainder else 0)
        split_data = data[start_index:end_index]
        start_index = end_index

        output_filepath = os.path.join(output_dir, f"{base_filename}_part{i + 1}.json")
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            json.dump(split_data, output_file, indent=4)

    print(f"JSON file split into {num_parts} parts successfully.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_filepath = sys.argv[1]
        print (input_filepath)
        split_json_file2(input_filepath)
    elif len(sys.argv) == 3:
        input_filepath = sys.argv[1]
        num_parts = int(sys.argv[2])

        split_json_file(input_filepath, num_parts)