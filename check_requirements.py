import os

# Check if sdfasdfa.txt exists
if os.path.exists('sdfasdfa.txt'):
    print("sdfasdfa.txt exists")
    with open('sdfasdfa.txt', 'r') as f:
        content = f.read().strip()  # Strip whitespace and newlines
        if content == "rfsdgv gvbfds":
            print("File contains correct text")
        else:
            print(f"File contains incorrect text: '{content}'")
else:
    print("sdfasdfa.txt does not exist")
