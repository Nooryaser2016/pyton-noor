# Main.py

file_name = "students.txt"

# Write data
with open(file_name, 'a') as f:
    f.write("Roy - Math\n")
    f.write("Anna - Science\n")

# Read data
with open(file_name, 'r') as f:
    print(f.read())