# File Modificatio: Read & Write with Error Handling

def main():
    try:
        # Request user for the input filename
        input_filename = input("Enter the name of the file you want to read: ")

        # Open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content, for example let's make it UPPERCASE.
        modified_content = content.upper()

        # Ask user for a name to save the modified content in a separate file
        output_filename = input("Enter the name of the file to save the modified content: ")

        # Write and save the modified content into the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ Successfully created '{output_filename}' with the modified content!")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except IOError:
        print("Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
