import os

# Check if sdfasdfa.txt exists in root directory
if os.path.exists("sdfasdfa.txt"):
    print("File exists")
    with open("sdfasdfa.txt", "r") as f:
        content = f.read()
        print(f"File content: '{content}'")
        if content.strip() == "rfsdgv gvbfds":
            print("File has correct content")
        else:
            print(f"File has incorrect content: {content.strip()}")
else:
    print("File does not exist")
