# Task 2: Write and Append Data to a File
# Takes user input, writes to output.txt, appends data,
# and displays the final content

try:
    # Get user input
    user_input = input("Enter some data: ")
    
    # Write the input to output.txt (creates or overwrites the file)
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")
        print("Data written to output.txt")
    
    # Append additional data to the same file
    additional_data = input("Enter additional data to append: ")
    with open("output.txt", "a") as file:
        file.write(additional_data + "\n")
        print("Data appended to output.txt")
    
    # Read and display the final content of the file
    print("\n--- Final Content of output.txt ---")
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)
    
except IOError as e:
    print(f"Error: Could not perform file operations: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")