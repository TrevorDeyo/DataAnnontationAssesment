def decode(message_file):
    # Check if the input is a filename ending with '.txt'
    if message_file.endswith('.txt'):
        # If it's a filename, open the file and read its content
        with open(message_file, 'r') as file:
            file_string = file.read()
    else:
        # If it's not a filename, assume it's the actual message and assign it to file_string
        file_string = message_file

    # Split the file content into lines
    lines = file_string.split('\n')

    # Create an empty dictionary to store the keys
    keys = {}
    # Iterate through each line in the file
    for line in lines:
        # Check if the line is not empty
        if len(line) > 0:
            # Split the line into two parts: key and value
            line_split = line.split()
            # Convert the key to an integer and use it as the key in the dictionary
            # The value is the character corresponding to that key
            keys[int(line_split[0])] = line_split[1]

    # Sort the dictionary by keys in ascending order
    keys = dict(sorted(keys.items()))

    # Initialize a counter variable to keep track of the index for generating the cipher keys
    count = 1
    # Create an empty list to store the cipher keys
    cypher_keys = []

    # Iterate through each key in the sorted dictionary
    for key in keys:
        # If the counter is less than or equal to the number of keys
        if count <= len(keys):
            # Add the current count to the list of cipher keys
            cypher_keys.append(count)
            # Increment the count by the value of the current key plus 1
            count += key + 1

    # Initialize an empty string to store the decoded message
    solution = ""
    # Iterate through each cipher key
    for cypher_key in cypher_keys:
        # Append the character corresponding to the cipher key to the solution string
        solution += keys[cypher_key] + ' '

    # Return the decoded message
    return solution

# Example usage:
# Decode the message from the file 'coding_qual_input.txt'
print(decode('coding_qual_input.txt'))

# Read the content of the file 'coding_qual_input.txt'
with open('coding_qual_input.txt', 'r') as file:
    message = file.read()

# Decode the message from the file content
print(decode(message))
