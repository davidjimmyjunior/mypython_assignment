# File Creation
try:
    # Open "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")  # Writing a mix of strings and numbers
        file.write("End of file.")
except PermissionError:
    print("Permission denied to create the file.")
except FileNotFoundError:
    print("File not found.")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("\nAppending line 1.\n")
        file.write("67890\n")  # Writing a mix of strings and numbers
        file.write("Another appended line.")
except PermissionError:
    print("Permission denied to append to the file.")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Task completed.")
