import pandas as pd

def convert_text_to_excel(input_file, output_file):
    # Read the text file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Parse the content
    data = []
    for line in lines:
        # Split the line by comma (or whatever separator you're using)
        attributes = line.strip().split(',')
        data.append(attributes)

    # Create a DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])

    # Write to Excel
    df.to_excel(output_file, index=False)

    print(f"Conversion complete. Excel file saved as {output_file}")

# Usage
input_file = 'input.txt'
output_file = 'output.xlsx'
convert_text_to_excel(input_file, output_file)
