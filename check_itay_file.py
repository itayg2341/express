import os

file_path = "itay.txt"
expected_content = "opt"

# Check if file exists
if os.path.exists(file_path):
    print(f"File {file_path} exists")
    
    # Check content
    with open(file_path, 'r') as f:
        content = f.read().strip()
        if content == expected_content:
            print(f"File contains expected text: '{expected_content}'")
        else:
            print(f"ERROR: File contains unexpected text: '{content}' (expected: '{expected_content}')")
else:
    print(f"ERROR: File {file_path} does not exist")
