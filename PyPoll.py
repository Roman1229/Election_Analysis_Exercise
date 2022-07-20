# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recevied votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of election based on popular vote

# Resources/election_results.csv

import csv
import os
# Assign a variable for the file to load and the path.

file_to_load = "C:/Users/roman/OneDrive/Desktop/Election_Analysis_Exercise/Resources/election_results.csv"
# Open the election results and read the file.
with open(file_to_load, encoding = "cp1252") as election_data:

    # Print the file object.
     print(election_data.read())

# Create a filename variable to a direct or indirect path to the file.
file_to_save = "C:/Users/roman/OneDrive/Desktop/Election_Analysis_Exercise/Resources/election_analysis.txt"
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Read the file object with the reader function.
    file_reader = csv.reader("C:/Users/roman/OneDrive/Desktop/Election_Analysis_Exercise/Resources/election_results.csv")

# Print each row in the CSV file.
    for row in file_reader:
        print(row)

# Print the header row.
    headers = next(file_reader)
    print(headers)
 