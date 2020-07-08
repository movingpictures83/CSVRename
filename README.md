# CSVRename
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin that takes a CSV file and renames rows or columns (user choice) to values from a second CSV file.

The plugin takes as input a TXT file of keyword-value pairs, tab-delimited:
replace (rows or columns)
file1 (file to do the replacement)
file2 (file to replace from)

file1 should be a CSV file with row and column names, one of which will be replaced.
file2 should be a CSV file of two columns.  The first should correspond to the data to be replaced in file1.  The second to their new names in the output file.

The output file is also CSV, with the rows or columns in file1 replaced accordingly.

