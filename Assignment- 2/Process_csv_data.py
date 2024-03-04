import pandas as pd

# Opening the file and counting the number of rows before "Data"
with open('problem_sheet.csv', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "Data" in line:
            skip = i
            break

# Save the headers
headers = lines[:skip+1]  # Include the "Data" line

# Read the CSV, skipping the rows before "Data"
df = pd.read_csv('problem_sheet.csv', skiprows=skip+1)

# Table for complementing a base
complement_table = str.maketrans('ATCG', 'TAGC')

# Performing operations on each string in the “index2” column
def reverse_complement(sequence):
    # A. Reverse the string
    reversed_sequence = sequence[::-1]
    
    # B. Complement the string using translation table
    complemented_sequence = reversed_sequence.translate(complement_table)
    
    return complemented_sequence

# Applying function to each element in index2_data and saving the results
df['reverse_complemented_strings'] = df['index2'].apply(reverse_complement)
# print(reverse_complemented_strings)a

# Saving the DataFrame to a new CSV file
df.to_csv('final_data_no_header.csv', index=False)

# Adding the headers back into the final CSV file
with open('final_data_no_header.csv', 'r') as f:
    data = f.read()
with open('final_data.csv', 'w') as f:
    f.writelines(headers)
    f.write(data)

