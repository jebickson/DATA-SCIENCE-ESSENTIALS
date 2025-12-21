import re
import csv

def validate_email(email):
    # Validate email using regular expression.
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_pattern, email))

def validate_phone(phone):
    # Validate 10-digit Indian phone number.
    phone_pattern = r"^[6-9]\d{9}$"
    return bool(re.match(phone_pattern, phone))

def clean_and_validate_csv(input_file, output_file):
    # Parse, clean, and validate CSV data.
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Email_Valid', 'Phone_Valid']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Clean and standardize name
            row['Name'] = row['Name'].strip().title()

            # Remove non-numeric characters from phone number
            row['phone.no'] = re.sub(r"[^\d]", "", row['phone.no'])

            # Validate phone and email
            row['Phone_Valid'] = validate_phone(row['phone.no'])
            row['Email_Valid'] = validate_email(row['Email'])

            writer.writerow(row)

# Run the function
clean_and_validate_csv(r'C:\Users\Happyy\Desktop\DATA SCIENCE ESSENTIALS\DATA-SCIENCE-ESSENTIALS\parsing_data.csv',
                       r'C:\Users\Happyy\Desktop\DATA SCIENCE ESSENTIALS\DATA-SCIENCE-ESSENTIALS\output.csv')

print("Data cleaning and validation complete. Check 'output.csv' for results.")
