with open('Readme.md', 'r') as f:
    content = f.read()
    
print("Current README structure:")
print("1. First few lines:")
print(content.split('\n')[:5])
print("\n2. Logo and title section:")
logo_section = content.split('\n')[:10]
for line in logo_section:
    print(line)
