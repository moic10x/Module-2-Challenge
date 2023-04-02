# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, data, header):
        """Saves the CSV file in the path provided.

    Args:
        csvpath (Path): The desired csv file path.
        data: the information desired to be stored in the path.
        header: inputs for the first row of the csv file labeling the information in each column.

    Returns:
        A csv file saved in the specified path.
    """
        with open(csvpath, 'w', newline='') as csvfile:
             csvwriter = csv.writer(csvfile)
             csvwriter.writerow(header)
             for row in data:
                  csvwriter.writerow(row)
                  
        return print("Your File Has Saved")

              

