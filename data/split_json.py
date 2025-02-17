import json
import os
import sys

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
    if len(sys.argv) != 3:
        print("Usage: python split_json.py <input_filepath> <num_parts>")
        sys.exit(1)

    input_filepath = sys.argv[1]
    num_parts = int(sys.argv[2])

    split_json_file(input_filepath, num_parts)