import os

# Check if file exists
if os.path.exists('sdfasdfa.txt'):
    print("File exists")
    with open('sdfasdfa.txt', 'r') as f:
        content = f.read()
        print(f"Content: {content}")
else:
    print("File does not exist")
