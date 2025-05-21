# A list of dictionaries, each representing a person's contact information
phonebook = [
    {'name': "ram", 'phone': 9888899998},
    {'name': "shyam", 'phone': 445555544},
    {'name': "hari", 'phone': 6665555444}
]

# Variable to store the matched contact (initialized as None)
recieve = None

# Loop through each entry in the phonebook
for key in phonebook:
    # Check if the current entry's name is 'hari'
    if key['name'] == "hari":
        recieve = key  # Store the matching dictionary in 'recieve'
        break  # Exit the loop once a match is found

# Print the contact details of the person named 'hari'
print(recieve)  # Output: {'name': 'hari', 'phone': 6665555444}
