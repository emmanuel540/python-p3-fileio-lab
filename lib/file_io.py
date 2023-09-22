def write_file(file_name, file_content):
    # Add the .txt extension to the file_name
    file_name_with_extension = str(file_name) + ".txt"

    # Open the file for writing
    with open(file_name_with_extension, "w") as file:
        # Write the content to the file
        file.write(file_content)

def append_file(file_name, append_content):
     # Add the .txt extension to the file_name
    file_name_with_extension = str(file_name) + ".txt"

    # Open the file for appending
    with open(file_name_with_extension, "a") as file:
        # Append the content to the file
        file.write(append_content)

def read_file(file_name):
    # Add the .txt extension to the file_name
    file_name_with_extension = str(file_name) + ".txt"

    try:
        # Open the file for reading
        with open(file_name_with_extension, "r") as file:
            # Read the content of the file
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        return "File not found."
    pass
