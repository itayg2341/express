import os

# Check if the file exists
if os.path.exists("sdfasdfa.txt"):
    print("File already exists")
    with open("sdfasdfa.txt", "r") as f:
        content = f.read()
        print(f"Current content: {content}")
else:
    print("File does not exist, creating it...")
    with open("sdfasdfa.txt", "w") as f:
        f.write("rfsdgv gvbfds")
    print("File created successfully!")
