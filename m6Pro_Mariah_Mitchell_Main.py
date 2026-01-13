# Created a program to analyze and clean customer feedback with different string methods. (Main.py)
# 24 November 2025
# CSC121 M6Pro
# Mariah Mitchell

import csv
import m6Pro_Mariah_Mitchell_Functions as fn

def main():
    '''
    Process customer feedback from a CSV file.
    
    Returns
    -------
    None.

    '''
    total = valid = invalid = pos_count = neg_count = 0
    # Reads each row from 'feedback.csv' file
    try:
        with open("feedback.csv", "r", encoding="utf-8") as file, \
             open("positive_cleaned_feedback.txt", "w", encoding="utf-8") as pos_file, \
             open("negative_cleaned_feedback.txt", "w", encoding="utf-8") as neg_file:

            reader = csv.reader(file)
            next(reader) # skip header

            for row in reader:
                total += 1
                if len(row) != 4:  #skip invalid rows
                    invalid += 1
                    continue

                name, email, product, feedback = row

                # Cleans the name, email, product and feedback text
                name = fn.clean_name(name)
                email = fn.clean_email(email)
                product = fn.clean_product(product)
                feedback = fn.clean_feedback(feedback)

                # Valdate names and email addresses
                if not fn.is_valid_name(name) or not fn.is_valid_email(email):
                    invalid += 1
                    continue

                valid += 1

                # Write to file as a feedback entry
                # Counts total, valid, invalid, positive, and negative entries
                if fn.contains_negative(feedback):
                    fn.write_entry(neg_file, name, email, product, feedback)
                    neg_count += 1
                else:
                    fn.write_entry(pos_file, name, email, product, feedback)
                    pos_count += 1

    except FileNotFoundError:
        print("feedback.csv not found.")
        return

    # Output summary
    print(f"Total entries processed: {total}")
    print(f"Valid entries: {valid}")
    print(f"Invalid entries skipped: {invalid}")
    print(f"Positive entries written: {pos_count}")
    print(f"Negative entries written: {neg_count}")


if __name__ == "__main__":
    main()