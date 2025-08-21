import os  # Import the os module to interact with the operating system

# Get the current working directory
directory = os.getcwd()  

# List all files and folders in the directory
contents = os.listdir(directory)  

# Print each item line by line
print(f"Contents of directory: {directory}\n")  
for item in contents:
    print(item)  # Print the name of each file and folder
 