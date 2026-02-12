# Task 1: Read a File and Handle Errors
# Opens and reads sample.txt, prints content line by line,
# and handles errors gracefully if the file doesn't exist

try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        print("File content:")
        # Read and print line by line
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.rstrip()}")
        
        if not lines:
            print("The file is empty.")

except FileNotFoundError:
    # Handle the case when the file does not exist
    print("Error: The file 'sample.txt' does not exist.")
    print("Please create the file and try again.")

except IOError as e:
    # Handle other IO related errors
    print(f"Error reading the file: {e}")

except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
