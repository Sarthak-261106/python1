file_name = "sample.txt"

try:
    with open(file_name, "r") as file:
        print("Reading file content:\n")

        line_no = 1
        for line in file:
            print(f"Line {line_no}: {line.strip()}")
            line_no += 1
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")